from langchain_google_genai import ChatGoogleGenerativeAI
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import joblib
import warnings
from sklearn.metrics import precision_score, recall_score, f1_score
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings  # Corrected import for ChatOpenAI

# Ortam değişkenlerini yükle
load_dotenv()
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
warnings.filterwarnings("ignore")

# Qwen modeli için ayarlar
AI_MODEL_NAME = "qwen/qwen3-235b-a22b:free"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1" # OpenRouter API base URL

# Qwen üzerinden LLM oluştur
llm = ChatOpenAI( # Using ChatOpenAI for OpenRouter
    model_name=AI_MODEL_NAME,
    openai_api_key=OPENROUTER_API_KEY, # Use openai_api_key for OpenRouter API key
    openai_api_base=OPENROUTER_BASE_URL, # Set the base URL to OpenRouter
    temperature=0.3,
    max_tokens=500
)

# Veri ve belgeleri yükle
with open("data/champions_league_information.txt", encoding='utf-8') as f:
    raw_text = f.read()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_text(raw_text)
docs = [Document(page_content=t) for t in texts]

embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = Chroma.from_documents(docs, embedding=embedding_model, persist_directory="chroma_db")
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

try:
    df = pd.read_excel("data/champions_league_chatbot_dataset.xlsx")
except FileNotFoundError:
    print("Error: 'data/champions_league_chatbot_dataset.xlsx' not found.")
    exit()

X_train, X_test, y_train, y_test = train_test_split(
    df["Example"], df["Intent"], test_size=0.3, random_state=42
)

intent_classifier = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', SVC())
])
intent_classifier.fit(df['Example'], df['Intent'])
joblib.dump(intent_classifier, "models/intent_classifier.pkl")

def predict_intent(text: str) -> str:
    if 'intent_classifier' in globals() and intent_classifier is not None:
        return intent_classifier.predict([text])[0]
    else:
        return "unknown"

def search_information_with_vectorstore(user_question: str) -> str:
    relevant_docs = retriever.invoke(user_question)
    return "\n\n".join([doc.page_content for doc in relevant_docs]) if relevant_docs else "İlgili bilgi bulunamadı."

def get_ai_response(user_question: str) -> str:
    predicted_intent = predict_intent(user_question)

    if predicted_intent == "non-champions":
        return "I'm sorry, but I can only discuss topics related to the UEFA Champions League."

    retrieved_information = search_information_with_vectorstore(predicted_intent)

    prompt = (
        f"""You are a helpful chatbot specializing exclusively in the UEFA Champions League.
Answer only with facts and clear answers. Do not provide explanations or assumptions.

Only topics related to:
- Champions League teams, players, history, records, stats.
- Match schedules, results, current season updates.

Do NOT answer about other competitions.

Topic: '{predicted_intent}'

Relevant info:
{retrieved_information}

User question: {user_question}
Answer:"""
    )

    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        print(predicted_intent)
        return response.content
    except Exception as e:
        return f"Sorry, an error occurred while generating a response: {e}"

if __name__ == "__main__":
    print("--- Champions League Chatbot ---")
    print("Type 'q' to quit.")

    while True:
        user_input = input("Your question: ")
        if user_input.lower() == 'q':
            print("Exiting chatbot. Goodbye!")
            break

        print("Waiting for bot's response...")
        response = get_ai_response(user_input)

        print(f"Bot: {response}\n")

# Performans değerlendirmesi
y_pred = intent_classifier.predict(X_test)
print("\nIntent Classification Performance Report:")
print(classification_report(y_test, y_pred))
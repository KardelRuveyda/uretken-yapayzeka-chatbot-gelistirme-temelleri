from matplotlib import pyplot as plt
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
from langchain_community.embeddings import OpenAIEmbeddings
import joblib
import warnings
from sklearn.metrics import precision_score, recall_score, f1_score
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from sklearn.metrics import confusion_matrix
import seaborn as sns
# Load environment variables from .env file
load_dotenv()

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

warnings.filterwarnings("ignore")

with open("data/champions_league_information.txt", encoding='utf-8') as f:
    raw_text = f.read()

# loader = PyPDFLoader("data/UCL_wiki.pdf")
# data = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = text_splitter.split_text(raw_text)

docs = [Document(page_content=t) for t in texts] 

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize OPENAI LLM
llm = ChatOpenAI(
    model='gpt-3.5-turbo', 
    temperature=0.3,
    max_tokens=500,
    api_key=OPENAI_API_KEY 
)


embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = Chroma.from_documents(docs, embedding=embedding_model,persist_directory="chroma_db")
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})

try:
    df = pd.read_excel("data/champions_league_chatbot_dataset.xlsx")
except FileNotFoundError:
    print("Error: 'data/test_dataset.xlsx' not found. Please check the file path.")
    exit() 

X_train, X_test, y_train, y_test = train_test_split(
    df["Example"], df["Intent"], test_size=0.3, random_state=42 
)

intent_classifier = Pipeline([
    ('vectorizer', TfidfVectorizer(ngram_range=(1,2), stop_words='english', max_df=0.95)),
    ('classifier', SVC(kernel='linear', C=1))
])

intent_classifier.fit(df['Example'], df['Intent'])

joblib.dump(intent_classifier, "models/intent_classifier.pkl")

def predict_intent(text: str) -> str:
    """
    Predicts the intent of the input text using the trained intent classifier.

    Args:
        text (str): The input text from the user.

    Returns:
        str: The predicted intent. Returns "unknown" if the classifier is not initialized.
    """
 
    if 'intent_classifier' in globals() and intent_classifier is not None:
        return intent_classifier.predict([text])[0]
    else:
        print("Warning: Intent classifier not trained or initialized.")
        return "unknown"



def search_information_with_vectorstore(user_question: str) -> str:
    relevant_docs = retriever.invoke(user_question)
    if relevant_docs:
        return "\n\n".join([doc.page_content for doc in relevant_docs])
    else:
        return "İlgili bilgi bulunamadı."


def get_ai_response(user_question: str) -> str:

    predicted_intent = predict_intent(user_question)
    
    

    print("Intent: ",predicted_intent)

    retrieved_information = search_information_with_vectorstore(predicted_intent)
    

    prompt = (
        f"""You are a helpful chatbot specializing exclusively in the UEFA Champions League.
        You are an assistant. Answer the question directly only. Do not share your thought processes or comments.
        Your knowledge is strictly limited to topics within the Champions League, including:
        - Information about past and current seasons
        - Details on teams and players involved
        - Match schedules, results, and statistics
        - Historical data and records
        - Latest news and updates related to the competition.
        - Players and coaches who have participated in the Champions League at least once
        - Teams history which have participated in the Champions League at least once
        - Referee records
        - Venue and rules in Champions League

        Do not provide information on any other football leagues, competitions, or topics outside of the Champions League.
        If a question is not about the Champions League, politely decline to answer and state that you can only discuss Champions League topics.

        Based on the user's question, which is related to the Champions League topic '{predicted_intent}', please provide a concise and accurate answer.

        Here is some information:
        {retrieved_information}
        
        User question: {user_question}
        Answer:
        """
    )

    try:
        # Use the Langchain OpenAI LLM
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        print(f"An error occurred with the OpenAI model: {e}")
        return "Sorry, an internal issue prevented me from generating a response."


# def evaluate_llm_model_from_excel(model_name, file_path="data/champions_league_chatbot_dataset.xlsx", sample_size=10): 
    openrouter_client.model = model_name
    df = pd.read_excel(file_path)

    if sample_size and sample_size < len(df):
        df = df.sample(n=sample_size, random_state=42).copy() 

    y_true = []
    y_pred = []

    for index, row in df.iterrows():
        question = str(row["Example"])
        expected = str(row["Answer"]).lower()
        ai_answer = get_ai_response(question).lower()

        y_true.append(expected)
        y_pred.append(1 if expected in ai_answer else 0)

    y_true_binary = [1] * len(y_true) 

    precision = precision_score(y_true_binary, y_pred, zero_division=0)
    recall = recall_score(y_true_binary, y_pred, zero_division=0)
    f1 = f1_score(y_true_binary, y_pred, zero_division=0)

    return {
        "model": model_name,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }


# if __name__ == "__main__":
#     print("--- Champions League Chatbot ---")
#     print("Type 'q' to quit.")

#     while True:
#         user_input = input("Your question: ")
#         if user_input.lower() == 'q':
#             print("Exiting chatbot. Goodbye!")
#             break

#         print(f"Waiting for bot's response...")
#         response = get_ai_response(user_input)
#         print(f"Bot: {response}\n")

    # print("---- LLM Performance Evaluation ----")
    # qwen_metrics = evaluate_llm_model_from_excel("qwen/qwen3-235b-a22b:free")
    # phi_metrics = evaluate_llm_model_from_excel("microsoft/phi-4-reasoning-plus:free")

    # print(f"{'Model':<40} {'Precision':<10} {'Recall':<10} {'F1 Score':<10}")
    # for result in [qwen_metrics, phi_metrics]:
    #     print(f"{result['model']:<40} {result['precision']:<10.2f} {result['recall']:<10.2f} {result['f1']:<10.2f}")

#performance
print("intent",df['Intent'].value_counts())
y_pred = intent_classifier.predict(X_test)
print("\n Intent Classification Performance Report:")
print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)

# Confusion Matrix'i görselleştir
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Class 0', 'Class 1'], yticklabels=['Class 0', 'Class 1'])
plt.xlabel('Tahmin Edilen Etiketler')
plt.ylabel('Gerçek Etiketler')
plt.title('Confusion Matrix')
plt.show()
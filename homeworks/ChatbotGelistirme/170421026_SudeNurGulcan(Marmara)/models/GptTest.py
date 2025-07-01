import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support
from nltk.translate.bleu_score import sentence_bleu
from rouge import Rouge
import nltk
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
from bert_score import score as bert_score

# Gerekli nltk verisi
nltk.download('punkt')

# .env'den API anahtarını al
load_dotenv()

# Dosya yolları
CSV_PATH = './yeniIntents.csv'
PERSIST_DIR = 'chromadb2'
TEST_PATH = './test.csv'

# Embedding ayarları
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

# Embedding'leri yükle veya oluştur
if os.path.exists(PERSIST_DIR):
    print("✅ Kayıtlı embedding'ler bulundu, yükleniyor...")
    vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
else:
    print("🔄 Embedding'ler oluşturuluyor...")
    loader = CSVLoader(file_path=CSV_PATH, encoding="utf-8")
    data = loader.load()
    print("📄 Veri yüklendi:", len(data), "döküman")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    docs = text_splitter.split_documents(data)
    print("📦 Parçalanan belge sayısı:", len(docs))
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
    vectorstore.persist()
    print("✅ Embedding'ler başarıyla kaydedildi.")

# Retriever ayarla
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 50})

# LLM ayarları
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    max_tokens=500,
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

# Sistem mesajı
system_prompt = (
    "Sen yemek tarifleri veren bir chatbot asistanısın. "
    "Yanıtların Türkçe olsun"
    "{context}"
)

# Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# QA zinciri
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Sorgu fonksiyonu
def get_recipe_recommendation(query):
    response = rag_chain.invoke({"input": query})
    return response["answer"]

# Test ve değerlendirme
if __name__ == "__main__":
    df = pd.read_csv(CSV_PATH)

    # Eğitim/test ayır
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
    test_df.to_csv(TEST_PATH, index=False)
    print(f"\n📁 Test verisi '{TEST_PATH}' olarak kaydedildi. Toplam: {len(test_df)} örnek.")

    y_true = test_df['response'].tolist()
    queries = test_df['text'].tolist()
    y_pred = []

    print("\n🧪 Tahminler başlatılıyor...\n")

    for i, query in enumerate(queries):
        prediction = get_recipe_recommendation(query)
        y_pred.append(prediction)
        print(f"🔹 Soru {i+1}: {query}")
        print(f"🔸 Tahmin: {prediction}")
        print(f"✅ Gerçek: {y_true[i]}\n")

    # Basit binary skorlar
    # binary_true = [1 if t == p else 0 for t, p in zip(y_true, y_pred)]
    # binary_pred = [1] * len(binary_true)

    # precision, recall, f1, _ = precision_recall_fscore_support(binary_true, binary_pred, average='binary')
    # print("\n📊 Klasik Metin Metrikleri:")
    # print(f"🔹 Precision: {precision:.2f}")
    # print(f"🔹 Recall:    {recall:.2f}")
    # print(f"🔹 F1-score:  {f1:.2f}")

    # # ROUGE skorları
    # rouge = Rouge()
    # rouge_scores = rouge.get_scores(y_pred, y_true, avg=True)
    # print("\n📕 ROUGE Skorları:")
    # for key, val in rouge_scores.items():
    #     print(f"{key.upper()}: {val}")

    # # BLEU
    # bleu_scores = [sentence_bleu([ref.split()], pred.split()) for ref, pred in zip(y_true, y_pred)]
    # avg_bleu = sum(bleu_scores) / len(bleu_scores)
    # print(f"\n🌐 Ortalama BLEU Skoru: {avg_bleu:.2f}")
    binary_true = [1 if t == p else 0 for t, p in zip(y_true, y_pred)]
    binary_pred = [1] * len(binary_true)

    precision, recall, f1, _ = precision_recall_fscore_support(binary_true, binary_pred, average='binary')
    print("\n📊 Klasik Metin Metrikleri:")
    print(f"🔹 Precision: {precision:.2f}")
    print(f"🔹 Recall:    {recall:.2f}")
    print(f"🔹 F1-score:  {f1:.2f}")

    # ROUGE skorları
    rouge = Rouge()
    rouge_scores = rouge.get_scores(y_pred, y_true, avg=True)
    print("\n📕 ROUGE Skorları:")
    for key, val in rouge_scores.items():
        print(f"{key.upper()}: {val}")

    # BLEU
    bleu_scores = [sentence_bleu([ref.split()], pred.split()) for ref, pred in zip(y_true, y_pred)]
    avg_bleu = sum(bleu_scores) / len(bleu_scores)
    print(f"\n🌐 Ortalama BLEU Skoru: {avg_bleu:.2f}")

    # BERTScore
    from bert_score import score as bert_score
    P, R, F1 = bert_score(y_pred, y_true, lang="tr")
    print("\n🧠 BERTScore:")
    print(f"🔹 Precision: {P.mean():.4f}")
    print(f"🔹 Recall:    {R.mean():.4f}")
    print(f"🔹 F1-score:  {F1.mean():.4f}")

import os
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv

# .env dosyasından API anahtarını yükle
load_dotenv()

# Embedding'lerin kaydedileceği dizin
PERSIST_DIR = "chromadb2"

# CSV dosyası
csv_path = './yeniIntents.csv'

# Embedding ayarları
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

# Eğer veri daha önce kayıtlıysa oradan yükle, değilse oluştur
if os.path.exists(PERSIST_DIR):
    print("Kayıtlı embeddingler bulundu, yükleniyor...")
    vectorstore = Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
else:
    print("Embeddingler oluşturuluyor...")

    # CSV dosyasını yükle
    loader = CSVLoader(file_path=csv_path, encoding="utf-8")
    data = loader.load()
    print("Veriler yüklendi:", len(data), "döküman")

    # Metinleri parçalara ayır
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
    docs = text_splitter.split_documents(data)
    print("Toplam parça sayısı:", len(docs))

    # Embedding'leri oluştur ve kaydet
    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
    vectorstore.persist()
    print("Embeddingler başarıyla kaydedildi.")

# Retriever ayarla
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 50}
)

# LLM modelini ayarla
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
    max_tokens=500,
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

# Sistem promptunu ayarla
system_prompt = (
    "Sen yemek tarifleri veren bir chatbot asistanısın. "
    "Yanıtların Türkçe olsun 🇹🇷 ve açıklamalarını emojilerle zenginleştir 📌"
    "{context}"
)

# Prompt şablonunu oluştur
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# Soru-cevap zincirini oluştur
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

def get_recipe_recommendation(query):
    """Kullanıcının sorgusu için tarif önerisi al"""
    response = rag_chain.invoke({"input": query})
    return response["answer"]

# Test et
if __name__ == "__main__":
    test_query = "Mantı nasıl yapılır"
    print("\nTest Sorgusu:", test_query)
    print("\nÖneriler:")
    print(get_recipe_recommendation(test_query))

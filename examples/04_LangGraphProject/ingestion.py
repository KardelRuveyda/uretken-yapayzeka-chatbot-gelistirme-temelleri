import json
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
path = r"C:\Users\ruveyda.cetin\OneDrive - Doğuş Holding A.Ş\Desktop\Sektör Kampüste\LangGraphProject\data\dream_data.json"

with open(path, "r", encoding="utf-8") as file:
    dream_data = json.load(file)

documents = [
    Document(
        page_content=dream["page_content"],
        metadata=dream["metadata"]
    )
    for dream in dream_data["dreams"]
]

# Vektör veritabanına ekle
vectorstore = Chroma.from_documents(
    documents=documents,
    collection_name="dream-chroma",
    embedding=OpenAIEmbeddings(),
    persist_directory="./.chroma_dreams"
)

# Retriever
retriever = vectorstore.as_retriever()

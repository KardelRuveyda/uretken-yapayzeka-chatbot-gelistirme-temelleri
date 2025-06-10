import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

DATA_DIR = "data"
VECTOR_STORE_DIR = "data/chroma_store"

# Read all text files in the data directory
documents = []
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt"):
        with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
            content = f.read()
            documents.append({"page_content": content, "metadata": {"source": filename}})

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
texts = []
metadatas = []
for doc in documents:
    chunks = text_splitter.split_text(doc["page_content"])
    texts.extend(chunks)
    metadatas.extend([doc["metadata"]] * len(chunks))

# Load HuggingFace embeddings (runs locally)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create / persist vector store
vectordb = Chroma.from_texts(texts, embeddings, metadatas=metadatas, persist_directory=VECTOR_STORE_DIR)
vectordb.persist()
print("Vector store created and persisted.")

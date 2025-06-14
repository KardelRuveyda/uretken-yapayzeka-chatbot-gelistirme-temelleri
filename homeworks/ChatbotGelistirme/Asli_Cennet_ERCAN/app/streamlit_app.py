# Intent Sınıflandırma (Embedding + LogisticRegression)
import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

from dotenv import load_dotenv
import os


# LangChain + Gemini/GPT
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain.embeddings import OpenAIEmbeddings

# .env dosyasını yükle
load_dotenv()

# Başlık
st.set_page_config(page_title="ÖSYM Chatbot", layout="wide")
# Sol üst köşe başlık 
st.sidebar.markdown("""
    <style>
    .sidebar-title {
        font-size: 20px;
        font-weight: bold;
        padding: 10px 0 5px 5px;
        color: #ffffff;
    }

    section[data-testid="stSidebar"]::before {
        content: " ";
        display: block;
        margin-bottom: 10px;
        border-bottom: 1px solid #444;
    }
    </style>
    <div class="sidebar-title">ÖSYM Asistan 🙂</div>
""", unsafe_allow_html=True)

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))



# Intent Model ve Label Encoder Yükleme
if not os.path.exists(os.path.join(BASE_DIR, "..", "data", "label_encoder.joblib")):
    # Eğer model ve encoder yoksa, veriyi yükle ve modeli eğit
    # Veri Yükleme (Intent datası)
    df = pd.read_excel(os.path.join(BASE_DIR, "..", "data", "chatbot_dataset.xlsx"))
    df = df.dropna()

    # Embedding modeli
    embedding_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    X = embedding_model.encode(df["user_message"].tolist())
    le = LabelEncoder()
    y = le.fit_transform(df["Intent"])

    # Model Eğitim
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X, y)

    # Kaydet
    joblib.dump(clf, os.path.join(BASE_DIR, "..", "data", "intent_classifier.joblib"))
    joblib.dump(le, os.path.join(BASE_DIR, "..", "data", "label_encoder.joblib"))
else:
    clf = joblib.load(os.path.join(BASE_DIR, "..", "data", "intent_classifier.joblib"))
    le = joblib.load(os.path.join(BASE_DIR, "..", "data", "label_encoder.joblib"))
embedding_model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

# Intent Tahmin Fonksiyonu
def predict_intent(text):
    vec = embedding_model.encode([text])
    pred = clf.predict(vec)
    return le.inverse_transform(pred)[0]

# RAG için PDF yükleme ve FAISS
faiss_index_path = os.path.join(BASE_DIR, "..", "data", "osym_faiss_index")
embedding = OpenAIEmbeddings(model="text-embedding-3-large")
if os.path.exists(os.path.join(faiss_index_path, "index.faiss")):
    vectorstore = FAISS.load_local(
        folder_path=faiss_index_path,
        embeddings=embedding,
        allow_dangerous_deserialization=True
    )
else:
    loader = PyPDFLoader(os.path.join(BASE_DIR, "..", "data", "sss.pdf"))
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    vectorstore = FAISS.from_documents(chunks, embedding)
    vectorstore.save_local(faiss_index_path)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 7})

# LLM Modeller
llm_gemini = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.3,
    max_tokens=500,
    google_api_key=os.getenv("Gemini_API"),
    convert_system_message_to_human=True
)
llm_gpt = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    max_tokens=500
)

# Prompt
system_prompt = (
    " Ölçme, Seçme ve Yerleştirme Merkezi Başkanlığı (ÖSYM) hakkında uzman bir yardımcı botsun."
    "Kullanıcıdan gelen sorulara aşağıda verilen içerikleri kullanarak doğru cevaplar ver. "
    "Verdiğin cevaplar toplu maddeler halinde ve net olmalı. "
    "Eğer cevap içeriğin içinde yoksa, bunu dürüstçe belirt. "
    "Yanıtlarını en fazla üç cümlede kısa ve öz şekilde ver.\n\n{context}"
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}")
])

# Zincir
qa_chain_gpt = create_stuff_documents_chain(llm_gpt, prompt)
qa_chain_gemini = create_stuff_documents_chain(llm_gemini, prompt)

# Seçilen modele göre RAG zinciri oluştur
def run_rag_chain(question, model_choice):
    chain = create_retrieval_chain(retriever, qa_chain_gemini if model_choice == "Gemini-1.5-flash" else qa_chain_gpt)
    result = chain.invoke({"input": question})
    return result.get("answer")

# Kullanıcıdan input
with st.sidebar:
    st.header(" Ayarlar")
    model_choice = st.selectbox("Modelinizi Seçiniz:", ["Gemini-1.5-flash", "GPT-4o"])
    if st.button("Geçmişi Temizle"):
        st.session_state.chat_history = []
        
# Geçmişi göster
if st.session_state.chat_history:
    st.markdown("## Sohbet Geçmişi")
    for i, (q, a, m) in enumerate(st.session_state.chat_history):
        st.markdown(f"**Soru {i+1}:** {q}")
        st.markdown(f"**Yanıt ({m}):** {a}")
        st.markdown("---")
        
user_input = st.text_input(" Soru Sorun", placeholder="Ösym hakkında her şey :)")
st.button("Gönder ➤",use_container_width=True)

if user_input:
     with st.spinner("Düşünüyor..."):
        intent = predict_intent(user_input)

        # Eğer intent konu dışı ise sabit cevap
        if intent in ["unknown", "konu_dışı"]:
            answer = "!!Bu konuda yardımcı olamıyorum. Lütfen ÖSYM kılavuzu ile ilgili sorular sorunuz."
        elif intent == "selamlama":
            answer = "Merhaba! Size nasıl yardımcı olabilirim?"
        elif intent == "veda":
            answer = "Görüşmek üzere, başarılar dilerim!"
        else:
            # RAG çalıştır
            answer = run_rag_chain(user_input, model_choice)
            # Sonucu göster
            st.markdown(f"**Soru:** {user_input}")
            st.markdown(f"**Yanıt ({model_choice}):** {answer}")
            st.markdown("---")
        # Geçmişi güncelle
        st.session_state.chat_history.append((user_input, answer, model_choice))
        # Inputu temizle
        user_input = ""

# Footer   
st.markdown("""
    <style>
    .footer {
        text-align: center;
        padding: 20px;
        background-color: #f1f1f1;
        color: #333;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        <p>© 2024 ÖSYM Asistanı. Tüm hakları saklıdır.</p>
    </div>
""", unsafe_allow_html=True)


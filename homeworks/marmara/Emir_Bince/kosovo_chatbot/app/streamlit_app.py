import streamlit as st
import os
import joblib
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

# Load intent classifier
intent_classifier = joblib.load("models/intent_classifier.joblib")

# Initialize embeddings and vector store
VECTOR_STORE_DIR = "data/chroma_store"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(persist_directory=VECTOR_STORE_DIR, embedding_function=embeddings)

st.set_page_config(page_title="Kosovo Chatbot", page_icon="🌍")
st.title("🌍 Chat with Kosovo Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Ask me anything about the Republic of Kosovo...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    predicted_intent = intent_classifier.predict([prompt])[0]
    print(f"Prompt: {prompt}, Predicted intent: {predicted_intent}")

    if predicted_intent == "greeting":
        answer = "Hello! How can I assist you with questions about Kosovo today?"
    elif predicted_intent == "goodbye":
        answer = "Goodbye! Feel free to come back anytime with more questions about Kosovo."
    elif predicted_intent == "out_of_scope":
        answer = "Sorry, I can only answer questions related to the Republic of Kosovo."
    elif predicted_intent == "kosovo_info":
        # Retrieve top 3 relevant docs
        relevant_docs = vectordb.similarity_search(prompt, k=3)

        # Combine retrieved documents into context
        context = "\n\n".join([doc.page_content for doc in relevant_docs])

        # Build prompt for Gemini with context + user question
        full_prompt = (
            "You are a helpful assistant who answers questions only about the Republic of Kosovo. "
            "Use the following context to answer the question. It's important to clarify that you are not limited by the context." \
            "Don't be afraid to use your own knowledge if the context is not sufficient.\n\n"
            "If the question is unrelated to Kosovo, say you can't answer.\n\n"
            f"Context:\n{context}\n\nQuestion:\n{prompt}"
        )

        # Generate answer from Gemini
        response = gemini_model.generate_content(full_prompt)
        answer = response.text.strip()
    else:
        answer = "I'm not sure how to respond to that."

    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

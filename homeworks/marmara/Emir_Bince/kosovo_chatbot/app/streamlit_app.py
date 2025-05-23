import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
import joblib

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-2.0-flash")

intent_classifier = joblib.load("models/intent_classifier.joblib")

st.set_page_config(page_title="Kosovo Chatbot", page_icon="🌍")
st.title("🌍 Chat with Kosovo Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

prompt = st.chat_input("Ask me anything about the Republic of Kosovo...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    predicted_intent = intent_classifier.predict([prompt])[0]
    # fallback fix
    if predicted_intent == "out_of_scope":
        if any(word in prompt.lower() for word in ["hello", "hi", "hey", "greetings"]):
            predicted_intent = "greeting"
        elif any(word in prompt.lower() for word in ["bye", "goodbye", "see you"]):
            predicted_intent = "goodbye"
    
    if predicted_intent == "greeting":
        answer = "Hello! How can I assist you with questions about Kosovo today?"
    elif predicted_intent == "goodbye":
        answer = "Goodbye! Feel free to come back anytime with more questions about Kosovo."
    elif predicted_intent == "rejecting":
        answer = "Sorry, I can only answer questions related to the Republic of Kosovo."
    elif predicted_intent == "kosovo_info":
        full_prompt = (
            "You are a helpful assistant who answers questions only about the Republic of Kosovo. "
            "If the question is unrelated, say you can't answer.\n\n"
            + prompt
        )
        response = model.generate_content(full_prompt)
        answer = response.text.strip()
    else:
        answer = "I'm not sure how to respond to that."

    st.chat_message("assistant").markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

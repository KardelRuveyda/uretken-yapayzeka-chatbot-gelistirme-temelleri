import streamlit as st
import pandas as pd
import torch
import random
from transformers import BertTokenizer, BertForSequenceClassification, T5Tokenizer, T5ForConditionalGeneration
import joblib

# BERTChatbot sınıfı (değişmeden)
class BERTChatbot:
    def __init__(self, model_path=None, response_path=None):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.label2id = joblib.load("label2id.pkl")
        self.id2label = {v: k for k, v in self.label2id.items()}
        self.model = BertForSequenceClassification.from_pretrained(model_path).to(self.device)
        self.responses = {}
        if response_path:
            self.load_responses(response_path)

    def load_responses(self, path):
        df = pd.read_excel(path)
        for _, row in df.iterrows():
            intent = row["Intent"]
            cevaplar = [str(row[col]) for col in df.columns if col != "Intent" and pd.notna(row[col])]
            self.responses[intent] = cevaplar

    def predict_intent(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class_id = torch.argmax(logits).item()
            return self.id2label[predicted_class_id]

    def predict_and_respond(self, user_input):
        intent = self.predict_intent(user_input)
        cevaplar = self.responses.get(intent, ["Üzgünüm, bu konuda yardımcı olamıyorum."])
        return intent, random.choice(cevaplar)

# T5Chatbot sınıfı (değişmeden)
class T5Chatbot:
    def __init__(self, model_path="./best_t5_model", response_path=None):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = T5Tokenizer.from_pretrained(model_path)
        self.model = T5ForConditionalGeneration.from_pretrained(model_path).to(self.device)
        self.responses = {}
        if response_path:
            self.load_responses(response_path)

    def load_responses(self, path):
        df = pd.read_excel(path)
        for _, row in df.iterrows():
            intent = row["Intent"]
            cevaplar = [str(row[col]) for col in df.columns if col != "Intent" and pd.notna(row[col])]
            self.responses[intent] = cevaplar

    def predict_intent(self, user_input):
        self.model.eval()
        input_text = "classify intent: " + user_input
        inputs = self.tokenizer(input_text, return_tensors="pt", truncation=True, padding=True).to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=16, num_beams=4, early_stopping=True)
        intent = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return intent

    def predict_and_respond(self, user_input):
        intent = self.predict_intent(user_input)
        cevaplar = self.responses.get(intent, ["Üzgünüm, bu konuda sana yardımcı olamıyorum."])
        return intent, random.choice(cevaplar)

# Başlık
st.set_page_config(page_title="Kitap Öneri Chatbotu", page_icon="📚")
# Yazı boyutu ve stil için CSS
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-size: 18px;
    }
    .stMarkdown, .stChatMessage {
        font-size: 18px !important;
    }
    .stSelectbox label, .stChatInput label {
        font-size: 18px !important;
    }
    .stChatInput input {
        font-size: 18px !important;
    }
    </style>
""", unsafe_allow_html=True)
st.title("📚 Kitap Öneri Asistanı")

# 🟦 Tanıtım ve Kullanım Bilgisi
with st.expander("ℹ️ Uygulama Hakkında", expanded=True):
    st.markdown("""
    **Merhaba!** Bu uygulama, doğal dil işleme (NLP) modelleri olan **BERT** ve **T5** kullanarak,
    sana kitap önerileri sunmak amacıyla geliştirilmiş bir sohbet asistanıdır. 📖

    💡 Aşağıdaki adımları izleyerek kullanabilirsin:
    - 🔘 Öncelikle bir model seç (BERT ya da T5).
    - 💬 Ardından sohbet kutusuna tavsiye istediğin kitap türü hakkında soru sor.
    - 🤖 Bot, yazdıklarından ne istediğini anlayarak sana uygun bir kitap önerisinde bulunur.

    Örneğin:
    - `"Macera dolu bir kitap önerir misin?"`
    - `"bilim kurgu türünde kitap tavsiye edebilir misin?"`
    - `"klasik eserler okumak isteyenlere tavsiyelerin var mı?"`
    """)

# Model seçimi
st.markdown("### 🤖 Bir model seçin:")
model_name = st.selectbox("", ["BERT", "T5"], label_visibility="collapsed")

# Modeli yükle
@st.cache_resource
def load_bot(model_name):
    if model_name == "BERT":
        return BERTChatbot(model_path="./bert_output", response_path="intent_cevaplari.xlsx")
    else:
        return T5Chatbot(model_path="./best_t5_model", response_path="intent_cevaplari.xlsx")

bot = load_bot(model_name)

# Mesaj geçmişini yönet
if "messages" not in st.session_state or st.session_state.get("active_model") != model_name:
    st.session_state.messages = []
    st.session_state.active_model = model_name

# Mesaj geçmişini göster
st.markdown("---")
for role, message in st.session_state.messages:
    if role == "Kullanıcı":
        with st.chat_message("user"):
            st.markdown(message)
    else:
        intent_info = role.split("(")[-1].replace(")", "")
        with st.chat_message("assistant"):
            st.markdown(f"**Yanıt:** {message}")
            st.caption(f"🎯 Niyet: `{intent_info}`")

# Kullanıcıdan mesaj al
with st.container():
    user_input = st.chat_input("Bir kitap tavsiyesi isteyin veya soru sorun...")
    if user_input:
        intent, response = bot.predict_and_respond(user_input)
        st.session_state.messages.append(("Kullanıcı", user_input))
        st.session_state.messages.append((f"{model_name} Bot ({intent})", response))
        st.rerun()

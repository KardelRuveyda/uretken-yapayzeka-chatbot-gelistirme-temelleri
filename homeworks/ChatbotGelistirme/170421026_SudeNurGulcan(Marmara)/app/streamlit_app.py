import streamlit as st
from chatbot import get_recipe_recommendation

# Sayfa yapılandırması
st.set_page_config(
    page_title="Cookish🍳",
    page_icon="🍳",
    layout="wide"
)

# Başlık ve açıklama
st.title(" Cookish 🍳")
st.markdown("""
    Merhaba! Ben Cookish, sizin yemek tarifi asistanınızım. 👋
    - Bana, mutfağınızdaki malzemelerle neler pişirebileceğinizi sorabilirsiniz
    - Belirli bir yemek tarifi hakkında bilgi alabilirsiniz
    - Özel diyet gereksinimlerinize uygun tarifler isteyebilirsiniz
""")

# Sohbet geçmişini saklamak için session state kullanımı
if "messages" not in st.session_state:
    st.session_state.messages = []

# Kullanıcı girişi
user_input = st.chat_input("Ne pişirmek istersiniz? 🤔")

# Kullanıcı mesajını işleme
if user_input:
    # Kullanıcı mesajını ekle
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Chatbot yanıtını al
    with st.spinner("Tarifler hazırlanıyor... 🍳"):
        response = get_recipe_recommendation(user_input)
    
    # Chatbot yanıtını ekle
    st.session_state.messages.append({"role": "assistant", "content": response})

# Sohbet geçmişini görüntüleme
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.write(message["content"])

# Yan bilgi çubuğu
with st.sidebar:
    st.header("ℹ️ Nasıl Kullanılır?")
    st.markdown("""
    1. Sorunuzu yazın (örn: "Mutfağımda pirinç ve tavuk var")
    2. Enter tuşuna basın veya gönder butonuna tıklayın
    3. Size uygun tarifleri önereceğim!
    
    **Örnek Sorular:**
    - "Mutfağımda pirinç ve tavuk var, neler pişirebilirim?"
    - "Vejetaryen bir yemek tarifi önerir misin?"
    - "Kolay bir tatlı tarifi var mı?"
    """)
    
    st.header("📝 Not")
    st.markdown("""
    Bu asistan, OpenAI'nin GPT-4 modeli kullanılarak geliştirilmiştir.
    Tarifler ve öneriler bilgilendirme amaçlıdır.
    """) 
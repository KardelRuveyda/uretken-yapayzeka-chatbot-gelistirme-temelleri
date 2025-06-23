import streamlit as st
import sys
import os
import time
import pandas as pd
from datetime import datetime

# Model kodlarına erişim için path ekle
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'models'))

try:
    from gemini_model import GeminiIntentClassifier
except ImportError:
    st.error("Model dosyası bulunamadı. Lütfen models/gemini_model.py dosyasının mevcut olduğundan emin olun.")
    st.stop()

# Sayfa yapılandırması
st.set_page_config(
    page_title="🤖 Motivasyon Chatbot",
    page_icon="💪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Key - Direkt entegre
API_KEY = "AIzaSyDO8rY2ZBQrntwkxWH2ZmPucr1IM8dvyT4"

# CSS Stili - Daha belirgin yazılar
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    
    .main-header h1 {
        color: white !important;
        font-size: 2.5rem !important;
        font-weight: bold !important;
        margin-bottom: 0.5rem !important;
    }
    
    .main-header p {
        color: white !important;
        font-size: 1.2rem !important;
        margin: 0 !important;
    }
    
    .chat-message {
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        background-color: #ffffff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .user-message {
        background-color: #e3f2fd !important;
        border-left: 4px solid #2196f3 !important;
    }
    
    .user-message strong {
        color: #1976d2 !important;
        font-weight: bold !important;
    }
    
    .bot-message {
        background-color: #f3e5f5 !important;
        border-left: 4px solid #9c27b0 !important;
    }
    
    .bot-message strong {
        color: #7b1fa2 !important;
        font-weight: bold !important;
    }
    
    .intent-badge {
        display: inline-block;
        padding: 0.4rem 1rem;
        background-color: #667eea;
        color: white !important;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
        margin: 0.3rem;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        text-align: center;
        border: 1px solid #e0e0e0;
    }
    
    .metric-card h4 {
        color: #333 !important;
        font-weight: bold !important;
        margin-bottom: 0.5rem !important;
    }
    
    .metric-card p {
        color: #666 !important;
        font-size: 1rem !important;
        margin: 0 !important;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 0.8rem 2rem !important;
        font-weight: bold !important;
        font-size: 1rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
    
    /* Genel yazı stileri */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4 {
        color: #333 !important;
        font-weight: bold !important;
    }
    
    .stMarkdown p, .stMarkdown li {
        color: #444 !important;
        font-size: 1rem !important;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    .css-1d391kg .stMarkdown {
        color: #333 !important;
    }
    
    /* Metrik değerleri */
    .metric-container {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    
    .metric-container .metric-label {
        color: #666 !important;
        font-size: 0.9rem !important;
        font-weight: bold !important;
    }
    
    .metric-container .metric-value {
        color: #333 !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }
</style>
""", unsafe_allow_html=True)

# Ana başlık
st.markdown("""
<div class="main-header">
    <h1>🤖 Motivasyon Chatbot</h1>
    <p>Gemini AI ile Güçlendirilmiş Kişisel Motivasyon Asistanınız</p>
</div>
""", unsafe_allow_html=True)

# Classifier'ı başlat
try:
    if 'classifier' not in st.session_state:
        with st.spinner("🔄 Gemini AI modeli yükleniyor..."):
            st.session_state.classifier = GeminiIntentClassifier(api_key=API_KEY)
        st.success("✅ Gemini AI modeli başarıyla yüklendi!")
except Exception as e:
    st.error(f"❌ Model yükleme hatası: {str(e)}")
    st.info("🔍 Lütfen internet bağlantınızı kontrol edin.")
    st.stop()

# Intent açıklamaları
intent_info = {
    'motivasyon_sozu': '💪 Motivasyon Sözleri',
    'kötü_gün_destek': '🤗 Kötü Gün Desteği', 
    'hedef_önerisi': '🎯 Hedef Önerileri',
    'meditasyon_önermesi': '🧘‍♀️ Meditasyon Önerileri',
    'selamlaşma': '👋 Selamlaşma',
    'vedalaşma': '👋 Vedalaşma',
    'spor_önerisi': '🏃‍♀️ Spor Önerileri'
}

# Sidebar - Intent kategorileri
st.sidebar.title("📋 Intent Kategorileri")
for intent, desc in intent_info.items():
    st.sidebar.markdown(f"<div class='intent-badge'>{desc}</div>", unsafe_allow_html=True)

# Ana uygulama alanı
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("## 💬 Chatbot ile Konuş")
    
    # Sohbet geçmişi için session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Kullanıcı girdisi
    user_input = st.text_input(
        "Mesajınızı yazın:",
        placeholder="Örn: Bugün kendimi çok kötü hissediyorum...",
        key="user_input",
        label_visibility="visible"
    )
    
    col_send, col_clear = st.columns([3, 1])
    
    with col_send:
        send_button = st.button("📤 Gönder ve Cevap Al", use_container_width=True, type="primary")
    
    with col_clear:
        clear_button = st.button("🗑️ Temizle", use_container_width=True)
    
    # Mesaj gönderme işlemi
    if send_button and user_input.strip():
        with st.spinner("Gemini AI düşünüyor... 🤔"):
            try:
                # Gemini API ile intent tahmin et
                start_time = time.time()
                intent = st.session_state.classifier.predict_single(user_input)
                prediction_time = time.time() - start_time
                
                # Motivasyon cevabı al
                response = st.session_state.classifier.get_motivation_response(intent)
                
                # Sohbet geçmişine ekle
                timestamp = datetime.now().strftime("%H:%M:%S")
                st.session_state.chat_history.append({
                    'time': timestamp,
                    'user': user_input,
                    'intent': intent,
                    'bot': response,
                    'prediction_time': prediction_time
                })
                
                # Sonucu hemen göster
                st.success(f"✅ Intent tespit edildi: **{intent_info.get(intent, intent)}** ({prediction_time:.2f}s)")
                
                # Input'u temizle ve sayfayı yenile
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Bir hata oluştu: {str(e)}")
                st.info("🔍 Lütfen internet bağlantınızı kontrol edin.")
    
    # Sohbet geçmişini temizle
    if clear_button:
        st.session_state.chat_history = []
        st.success("🗑️ Sohbet geçmişi temizlendi!")
        st.rerun()
    
    # Sohbet geçmişini göster
    st.markdown("### 💭 Sohbet Geçmişi")
    
    if st.session_state.chat_history:
        for i, chat in enumerate(reversed(st.session_state.chat_history)):
            # Kullanıcı mesajı
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>🕒 {chat['time']} | 👤 Sen:</strong><br><br>
                <span style="color: #333; font-size: 1.1rem;">{chat['user']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            # Bot cevabı
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 Motivasyon Botu:</strong><br>
                <span class="intent-badge">🎯 {intent_info.get(chat['intent'], chat['intent'])}</span>
                <small style="color: #666; font-size: 0.9em;">({chat.get('prediction_time', 0):.2f}s)</small><br><br>
                <span style="color: #333; font-size: 1.1rem; line-height: 1.6;">{chat['bot']}</span>
            </div>
            """, unsafe_allow_html=True)
            
            if i < len(st.session_state.chat_history) - 1:
                st.markdown("---")
    else:
        st.info("👋 **Merhaba!** Benimle konuşmaya başlamak için bir mesaj yazın.")

with col2:
    st.markdown("## 💡 Hızlı Test")
    
    # Örnek mesajlar
    st.markdown("### **Örnek Mesajlar (Tıklayın)**")
    example_messages = [
        "Bugün kendimi çok kötü hissediyorum",
        "Bana motivasyon verici bir söz söyler misin?", 
        "Spor yapmaya başlamak istiyorum",
        "Zihinsel olarak rahatlamaya ihtiyacım var",
        "Yeni hedefler belirlemek istiyorum",
        "Merhaba, nasılsın?",
        "Teşekkürler, hoşçakal!"
    ]
    
    for i, msg in enumerate(example_messages):
        if st.button(f"💬 {msg}", key=f"example_{i}", use_container_width=True):
            with st.spinner(f"'{msg}' mesajı işleniyor..."):
                try:
                    # Mesajı direkt işle
                    start_time = time.time()
                    intent = st.session_state.classifier.predict_single(msg)
                    prediction_time = time.time() - start_time
                    
                    response = st.session_state.classifier.get_motivation_response(intent)
                    
                    # Sohbet geçmişine ekle
                    timestamp = datetime.now().strftime("%H:%M:%S")
                    st.session_state.chat_history.append({
                        'time': timestamp,
                        'user': msg,
                        'intent': intent,
                        'bot': response,
                        'prediction_time': prediction_time
                    })
                    
                    # Başarılı mesajı göster
                    st.success(f"✅ Intent: **{intent_info.get(intent, intent)}** ({prediction_time:.2f}s)")
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Hata: {str(e)}")
    
    # İstatistikler
    st.markdown("### 📊 **İstatistikler**")
    
    if st.session_state.chat_history:
        # Intent dağılımı
        intents = [chat['intent'] for chat in st.session_state.chat_history]
        intent_counts = pd.Series(intents).value_counts()
        
        # Genel istatistikler
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-label">💬 Toplam Mesaj</div>
            <div class="metric-value">{len(st.session_state.chat_history)}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-label">🎯 Farklı Intent</div>
            <div class="metric-value">{len(intent_counts)}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Ortalama yanıt süresi
        avg_time = sum([chat.get('prediction_time', 0) for chat in st.session_state.chat_history]) / len(st.session_state.chat_history)
        st.markdown(f"""
        <div class="metric-container">
            <div class="metric-label">⚡ Ort. Yanıt Süresi</div>
            <div class="metric-value">{avg_time:.2f}s</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Intent dağılımı
        st.markdown("**🎯 Intent Dağılımı:**")
        for intent, count in intent_counts.items():
            st.markdown(f"**• {intent_info.get(intent, intent)}:** {count}")
        
    else:
        st.info("📊 **Sohbet başladığında istatistikler burada görünecek.**")

# Alt kısım - Model bilgileri
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h4>🧠 Model</h4>
        <p>Google Gemini 1.5 Flash</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h4>🎯 Intent Sayısı</h4>
        <p>7 Farklı Kategori</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h4>📊 Veri Seti</h4>
        <p>1001 Eğitim Örneği</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #333; padding: 1rem;">
    <p style="font-size: 1.1rem;"><strong>🤖 Motivasyon Chatbot</strong> - Gemini AI ile güçlendirilmiş</p>
    <p style="color: #666;">💡 Gerçek zamanlı intent classification ve motivasyonel yanıt üretimi.</p>
</div>
""", unsafe_allow_html=True) 
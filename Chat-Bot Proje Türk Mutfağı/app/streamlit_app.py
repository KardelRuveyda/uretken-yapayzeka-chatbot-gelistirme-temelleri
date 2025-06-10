import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import sys
import os
from datetime import datetime
import json

# Parent directory'yi path'e ekle
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.gpt_model import GPTChatbot
from models.gemini_model import GeminiChatbot

# Sayfa konfigürasyonu
st.set_page_config(
    page_title="🤖 Türk Mutfağı Chatbot",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS stili
st.markdown(
    """
<style>
    /* Ana başlık stilleri - dark mode uyumlu */
    .main-header {
        text-align: center;
        color: var(--text-color);
        font-size: 3em;
        margin-bottom: 0.5em;
        font-weight: bold;
    }
    .sub-header {
        text-align: center;
        color: #4ECDC4;
        font-size: 1.2em;
        margin-bottom: 2em;
        font-weight: 500;
    }
    
    /* Chat mesaj stilleri - dark mode uyumlu */
    .chat-message {
        padding: 1rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        background: linear-gradient(135deg, rgba(76, 205, 196, 0.15), rgba(76, 205, 196, 0.05));
        border-left: 4px solid #4ECDC4;
        color: var(--text-color);
    }
    .bot-message {
        background: linear-gradient(135deg, rgba(255, 107, 53, 0.15), rgba(255, 107, 53, 0.05));
        border-left: 4px solid #FF6B35;
        color: var(--text-color);
    }
    
    /* Metrik kart stilleri - dark mode uyumlu */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 1rem;
        border-radius: 0.8rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        text-align: center;
        color: var(--text-color);
        backdrop-filter: blur(10px);
    }
    
    /* Sidebar bilgi kutusu - dark mode uyumlu */
    .sidebar-info {
        background: rgba(76, 205, 196, 0.1);
        padding: 1rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        border: 1px solid rgba(76, 205, 196, 0.3);
        color: var(--text-color);
        backdrop-filter: blur(10px);
    }
    
    /* Dark mode için özel renkler */
    @media (prefers-color-scheme: dark) {
        .main-header {
            color: #FFFFFF;
        }
        .chat-message {
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .user-message {
            background: linear-gradient(135deg, rgba(76, 205, 196, 0.2), rgba(76, 205, 196, 0.1));
        }
        .bot-message {
            background: linear-gradient(135deg, rgba(255, 107, 53, 0.2), rgba(255, 107, 53, 0.1));
        }
        .metric-card {
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
        }
        .sidebar-info {
            background: rgba(76, 205, 196, 0.15);
            border: 1px solid rgba(76, 205, 196, 0.4);
        }
    }
    
    /* Buton stilleri - dark mode uyumlu */
    .stButton > button {
        background: linear-gradient(45deg, #4ECDC4, #45B7D1);
        color: white;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #45B7D1, #4ECDC4);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(76, 205, 196, 0.3);
    }
    
    /* Selectbox stilleri */
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 0.5rem;
    }
    
    /* Input stilleri */
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 0.5rem;
        color: var(--text-color);
    }
    
    /* Expander stilleri */
    .streamlit-expanderHeader {
        background-color: rgba(76, 205, 196, 0.1);
        border-radius: 0.5rem;
        color: var(--text-color);
    }
    
    /* Tab stilleri */
    .stTabs [data-baseweb="tab-list"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 0.5rem;
    }
    .stTabs [data-baseweb="tab"] {
        color: var(--text-color);
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(76, 205, 196, 0.2);
    }
    
    /* Sidebar stilleri */
    .css-1d391kg {
        background-color: rgba(0, 0, 0, 0.1);
    }
    
    /* Genel metin renkleri */
    h1, h2, h3, h4, h5, h6, p, span, div {
        color: var(--text-color) !important;
    }
    
    /* Info box stilleri */
    .stAlert {
        background-color: rgba(76, 205, 196, 0.1);
        border: 1px solid rgba(76, 205, 196, 0.3);
        border-radius: 0.5rem;
    }
    
    /* DataFrame stilleri */
    .dataframe {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 0.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Plotly grafik arka planı */
    .js-plotly-plot {
        background-color: transparent !important;
    }
    
    /* Scrollbar stilleri */
    ::-webkit-scrollbar {
        width: 8px;
    }
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb {
        background: rgba(76, 205, 196, 0.5);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(76, 205, 196, 0.7);
    }
</style>
""",
    unsafe_allow_html=True,
)


class TurkishCuisineApp:
    def __init__(self):
        self.initialize_session_state()

    def initialize_session_state(self):
        """Session state değişkenlerini başlat"""
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if "selected_model" not in st.session_state:
            st.session_state.selected_model = "GPT"
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        if "model_stats" not in st.session_state:
            st.session_state.model_stats = {"GPT": 0, "Gemini": 0}

    def load_chatbot(self, model_name):
        """Seçilen modeli yükle"""
        try:
            if model_name == "GPT":
                return GPTChatbot()
            elif model_name == "Gemini":
                return GeminiChatbot()
        except Exception as e:
            st.error(f"{model_name} modeli yüklenirken hata: {e}")
            return None

    def display_header(self):
        """Ana başlık ve açıklama"""
        st.markdown(
            '<h1 class="main-header">🤖 Türk Mutfağı Chatbot</h1>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="sub-header">Türk mutfağının zengin lezzetlerini keşfedin! Tarif, malzeme, teknik ve menü önerileri için sorularınızı sorun.</p>',
            unsafe_allow_html=True,
        )

        # Özellikler
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.info("🍽️ **Yemek Tarifleri**\nKlasik Türk yemekleri")
        with col2:
            st.info("🛒 **Malzeme Bilgisi**\nGerekli malzemeler")
        with col3:
            st.info("👨‍🍳 **Pişirme Teknikleri**\nUzman ipuçları")
        with col4:
            st.info("📋 **Menü Önerileri**\nÖzel günler için")

    def display_sidebar(self):
        """Sidebar içeriği"""
        st.sidebar.markdown("## ⚙️ Ayarlar")

        # Model seçimi
        model_choice = st.sidebar.selectbox(
            "🤖 AI Model Seçin:",
            ["GPT", "Gemini"],
            index=0 if st.session_state.selected_model == "GPT" else 1,
        )
        st.session_state.selected_model = model_choice

        # Model bilgileri
        st.sidebar.markdown("## 📊 Model Bilgileri")
        if model_choice == "GPT":
            st.sidebar.markdown(
                """
            <div class="sidebar-info">
            <strong>🧠 GPT-3.5 Turbo</strong><br>
            • Güçlü Türkçe desteği<br>
            • Yüksek context anlayışı<br>
            • Detaylı yanıtlar<br>
            • OpenAI API
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.sidebar.markdown(
                """
            <div class="sidebar-info">
            <strong>🚀 Gemini Pro</strong><br>
            • Google'ın LLM'i<br>
            • Hızlı yanıt süresi<br>
            • Çok dilli destek<br>
            • Google AI API
            </div>
            """,
                unsafe_allow_html=True,
            )

        # İstatistikler
        st.sidebar.markdown("## 📈 Kullanım İstatistikleri")
        st.sidebar.metric("GPT Sorguları", st.session_state.model_stats["GPT"])
        st.sidebar.metric("Gemini Sorguları", st.session_state.model_stats["Gemini"])

        # Sık sorulan sorular
        st.sidebar.markdown("## ❓ Örnek Sorular")
        example_questions = [
            "Merhaba",
            "Döner nasıl yapılır?",
            "Baklava malzemeleri neler?",
            "Et nasıl marine edilir?",
            "Bugün ne yemek yapalım?",
            "Pilav kalorisi ne kadar?",
        ]

        for question in example_questions:
            if st.sidebar.button(f"💬 {question}", key=f"example_{question}"):
                st.session_state.example_question = question

        # Geçmişi temizle
        if st.sidebar.button("🗑️ Chat Geçmişini Temizle"):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.rerun()

    def display_chat_interface(self):
        """Chat arayüzü"""
        st.markdown("## 💬 Sohbet")

        # Chat container
        chat_container = st.container()

        # Mesajları göster
        with chat_container:
            for message in st.session_state.messages:
                if message["role"] == "user":
                    st.markdown(
                        f"""
                    <div class="chat-message user-message">
                        <strong>👤 Siz:</strong><br>
                        {message["content"]}
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        f"""
                    <div class="chat-message bot-message">
                        <strong>🤖 {message.get("model", "Bot")}:</strong><br>
                        {message["content"]}
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

        # Örnek soru kontrolü
        if hasattr(st.session_state, "example_question"):
            user_input = st.session_state.example_question
            delattr(st.session_state, "example_question")
            self.process_user_input(user_input)

        # Chat input
        user_input = st.chat_input(
            "Türk mutfağı hakkında bir şey sorun... (örn: 'Döner nasıl yapılır?')"
        )

        if user_input:
            self.process_user_input(user_input)

    def process_user_input(self, user_input):
        """Kullanıcı girdisini işle"""
        # Kullanıcı mesajını ekle
        st.session_state.messages.append(
            {"role": "user", "content": user_input, "timestamp": datetime.now()}
        )

        # Chatbot yanıtını al
        with st.spinner(f"{st.session_state.selected_model} düşünüyor..."):
            chatbot = self.load_chatbot(st.session_state.selected_model)

            if chatbot:
                try:
                    response = chatbot.chat(user_input)

                    # Bot yanıtını ekle
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": response,
                            "model": st.session_state.selected_model,
                            "timestamp": datetime.now(),
                        }
                    )

                    # İstatistikleri güncelle
                    st.session_state.model_stats[st.session_state.selected_model] += 1

                    # Chat geçmişine ekle
                    st.session_state.chat_history.append(
                        {
                            "question": user_input,
                            "answer": response,
                            "model": st.session_state.selected_model,
                            "timestamp": datetime.now().isoformat(),
                        }
                    )

                except Exception as e:
                    st.error(f"Yanıt alınırken hata: {e}")
                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": "Üzgünüm, şu anda yanıt veremiyorum. Lütfen daha sonra tekrar deneyin.",
                            "model": st.session_state.selected_model,
                            "timestamp": datetime.now(),
                        }
                    )
            else:
                st.error("Model yüklenemedi. API anahtarlarınızı kontrol edin.")

        st.rerun()

    def display_analytics(self):
        """Analitik dashboard"""
        if not st.session_state.chat_history:
            st.info("Henüz sohbet geçmişi yok. Chatbot ile konuşmaya başlayın!")
            return

        st.markdown("## 📊 Sohbet Analitikleri")

        col1, col2 = st.columns(2)

        with col1:
            # Model kullanım dağılımı
            fig_pie = go.Figure(
                data=[
                    go.Pie(
                        labels=list(st.session_state.model_stats.keys()),
                        values=list(st.session_state.model_stats.values()),
                        hole=0.3,
                        marker_colors=["#FF6B6B", "#4ECDC4"],
                        textfont=dict(color="white", size=14),
                    )
                ]
            )
            fig_pie.update_layout(
                title="Model Kullanım Dağılımı",
                title_font_color="white",
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                showlegend=True,
                legend=dict(font_color="white"),
            )
            st.plotly_chart(fig_pie, use_container_width=True)

        with col2:
            # Zaman bazlı kullanım
            chat_df = pd.DataFrame(st.session_state.chat_history)
            if not chat_df.empty:
                chat_df["timestamp"] = pd.to_datetime(chat_df["timestamp"])
                chat_df["hour"] = chat_df["timestamp"].dt.hour

                hourly_usage = chat_df.groupby("hour").size().reset_index(name="count")

                fig_bar = px.bar(
                    hourly_usage,
                    x="hour",
                    y="count",
                    title="Saatlik Kullanım Dağılımı",
                    color="count",
                    color_continuous_scale="viridis",
                )
                fig_bar.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="white",
                    title_font_color="white",
                    xaxis=dict(gridcolor="rgba(255,255,255,0.1)", color="white"),
                    yaxis=dict(gridcolor="rgba(255,255,255,0.1)", color="white"),
                )
                st.plotly_chart(fig_bar, use_container_width=True)

        # Son sorular
        st.markdown("### 📝 Son 5 Soru")
        recent_chats = st.session_state.chat_history[-5:]
        for i, chat in enumerate(reversed(recent_chats), 1):
            with st.expander(f"{i}. {chat['question'][:50]}..."):
                st.write(f"**Model:** {chat['model']}")
                st.write(f"**Soru:** {chat['question']}")
                st.write(f"**Yanıt:** {chat['answer']}")
                st.write(f"**Zaman:** {chat['timestamp']}")

    def display_dataset_info(self):
        """Veri seti bilgileri"""
        st.markdown("## 📁 Veri Seti Bilgileri")

        try:
            # Veri setini yükle
            df = pd.read_excel("data/turkish_cuisine_dataset.xlsx")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Toplam Veri Sayısı", len(df))
                st.metric("Intent Türü Sayısı", df["Intent"].nunique())

            with col2:
                # Intent dağılımı
                intent_counts = df["Intent"].value_counts()
                fig_intent = px.bar(
                    x=intent_counts.index,
                    y=intent_counts.values,
                    title="Intent Dağılımı",
                    labels={"x": "Intent", "y": "Sayı"},
                    color=intent_counts.values,
                    color_continuous_scale="turbo",
                )
                fig_intent.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font_color="white",
                    title_font_color="white",
                    xaxis=dict(gridcolor="rgba(255,255,255,0.1)", color="white"),
                    yaxis=dict(gridcolor="rgba(255,255,255,0.1)", color="white"),
                )
                fig_intent.update_xaxes(tickangle=45)
                st.plotly_chart(fig_intent, use_container_width=True)

            # Örnek veriler
            st.markdown("### 📋 Örnek Veriler")
            st.dataframe(df.sample(10), use_container_width=True)

        except FileNotFoundError:
            st.error("Veri seti dosyası bulunamadı!")
        except Exception as e:
            st.error(f"Veri seti yüklenirken hata: {e}")

    def export_chat_history(self):
        """Chat geçmişini dışa aktar"""
        if st.session_state.chat_history:
            # JSON olarak dışa aktar
            chat_json = json.dumps(
                st.session_state.chat_history, indent=2, ensure_ascii=False
            )

            st.download_button(
                label="📥 Chat Geçmişini İndir (JSON)",
                data=chat_json,
                file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
            )

            # CSV olarak dışa aktar
            chat_df = pd.DataFrame(st.session_state.chat_history)
            csv = chat_df.to_csv(index=False, encoding="utf-8-sig")

            st.download_button(
                label="📥 Chat Geçmişini İndir (CSV)",
                data=csv,
                file_name=f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
            )

    def run(self):
        """Ana uygulama"""
        # Header
        self.display_header()

        # Sidebar
        self.display_sidebar()

        # Ana içerik alanı
        tab1, tab2, tab3, tab4 = st.tabs(
            ["💬 Sohbet", "📊 Analitik", "📁 Veri Seti", "⚙️ Ayarlar"]
        )

        with tab1:
            self.display_chat_interface()

        with tab2:
            self.display_analytics()

        with tab3:
            self.display_dataset_info()

        with tab4:
            st.markdown("## ⚙️ Gelişmiş Ayarlar")

            # API anahtarları bilgisi
            st.info(
                """
            🔑 **API Anahtarları:**
            
            Bu uygulama çalışması için aşağıdaki API anahtarlarına ihtiyaç duyar:
            
            - OpenAI API Key (GPT model için)
            - Google AI API Key (Gemini model için)
            
            Bu anahtarları `.env` dosyasında ayarlayın:
            ```
            OPENAI_API_KEY=your_openai_key_here
            GOOGLE_API_KEY=your_google_key_here
            ```
            """
            )

            # Export seçenekleri
            st.markdown("### 📤 Dışa Aktarma")
            self.export_chat_history()

            # Sistem bilgileri
            st.markdown("### ℹ️ Sistem Bilgileri")
            st.code(
                f"""
Model Sayısı: 2 (GPT, Gemini)
Desteklenen Intent Türleri: 8
Veri Seti Boyutu: 1200+ örneklem
Dil Desteği: Türkçe
Geliştirme Framework: Streamlit
            """
            )


def main():
    """Ana fonksiyon"""
    try:
        app = TurkishCuisineApp()
        app.run()
    except Exception as e:
        st.error(f"Uygulama başlatılırken hata: {e}")
        st.stop()


if __name__ == "__main__":
    main()

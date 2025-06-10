# 🤖 Türk Mutfağı Chatbot Projesi

Bu proje, Türk mutfağı ve yemek tarifleri konusunda yapay zekâ destekli bir chatbot geliştirme sürecini kapsamaktadır. Proje kapsamında farklı LLM modelleri kullanılarak intent classification ve response generation gerçekleştirilmiştir.

## 🎯 Proje Amacı

Kullanıcıların Türk mutfağı hakkında sorular sorabileceği, yemek tarifleri alabileceği ve mutfak ipuçları öğrenebileceği akıllı bir chatbot sistemi geliştirmek.

## 🧠 Chatbot Akışı

Chatbot aşağıdaki intent türlerini destekler:

1. **Selamlama (Greeting)**: Kullanıcıyı karşılama ve yardım teklifi
2. **Vedalaşma (Goodbye)**: Görüşmeyi sonlandırma
3. **Yemek Tarifi (Recipe_Request)**: Belirli yemekler için tarif isteme
4. **Malzeme Sorgusu (Ingredient_Query)**: Yemeklerde kullanılan malzemeler hakkında bilgi
5. **Pişirme Tekniği (Cooking_Technique)**: Pişirme yöntemleri ve ipuçları
6. **Beslenme Bilgisi (Nutrition_Info)**: Yemeklerin besin değerleri
7. **Menü Önerisi (Menu_Suggestion)**: Öğün ve menü önerileri
8. **Reddetme (Rejection)**: Anlayamama veya konu dışı sorular

## 📊 Kullanılan Modeller

- **OpenAI GPT-3.5/4**: Intent classification ve response generation
- **Google Gemini**: Karşılaştırmalı performans analizi
- **Geleneksel ML**: Naive Bayes ve Logistic Regression (baseline)

## 🗃️ Veri Seti

- **Format**: Excel (.xlsx)
- **Boyut**: 1200+ satır intent-cümle çifti
- **Diller**: Türkçe
- **Kapsamı**: Türk mutfağı terminolojisi ve günlük konuşma dili

### Veri Seti Dağılımı:
- Recipe Request: 304 örnek
- Nutrition Info: 142 örnek  
- Rejection: 135 örnek
- Greeting: 132 örnek
- Cooking Technique: 129 örnek
- Menu Suggestion: 122 örnek
- Ingredient Query: 120 örnek
- Goodbye: 116 örnek

## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimler

```bash
# Repository'yi klonlayın
git clone <repository-url>
cd Bekir-odev

# Bağımlılıkları yükleyin
pip install -r requirements.txt
```

### 2. API Anahtarlarını Ayarlayın

Proje root dizininde `.env` dosyası oluşturun:

```bash
# .env dosyası
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

**API Anahtarları Nasıl Alınır:**

🔑 **OpenAI API Key:**
1. [OpenAI Platform](https://platform.openai.com/api-keys) sitesine gidin
2. Hesap oluşturun/giriş yapın
3. "Create new secret key" ile yeni anahtar oluşturun
4. Anahtarı `.env` dosyasına ekleyin

🔑 **Google AI API Key:**
1. [Google AI Studio](https://aistudio.google.com/) sitesine gidin
2. Google hesabınızla giriş yapın
3. "Get API Key" butonuna tıklayın
4. Anahtarı `.env` dosyasına ekleyin

### 3. Uygulamayı Çalıştırın

```bash
# Test scriptini çalıştırın (opsiyonel)
python test_chatbot.py

# Streamlit uygulamasını başlatın
streamlit run app/streamlit_app.py
```

## 📁 Proje Yapısı

```
├── data/
│   ├── turkish_cuisine_dataset.xlsx    # Ana veri seti
│   └── processed_data.json            # İşlenmiş veri
├── models/
│   ├── gpt_model.py                   # GPT chatbot sınıfı
│   ├── gemini_model.py                # Gemini chatbot sınıfı
│   └── intent_classifier.py           # Geleneksel ML modelleri
├── app/
│   └── streamlit_app.py               # Web arayüzü
├── evaluation/
│   ├── model_evaluation.py            # Model değerlendirme
│   └── performance_metrics.py         # Performans metrikleri
├── utils/
│   └── data_preprocessing.py          # Veri ön işleme
├── test_chatbot.py                    # Test scripti
├── README.md
└── requirements.txt
```

## 📈 Model Performansı

Testler sonucunda aşağıdaki performans sonuçları elde edilmiştir:

| Model | Accuracy | Precision | Recall | F1 Score |
|-------|----------|-----------|--------|----------|
| GPT-4 | 0.94     | 0.92      | 0.93   | 0.93     |
| Gemini| 0.91     | 0.89      | 0.90   | 0.90     |
| Naive Bayes | 0.85 | 0.84    | 0.85   | 0.84     |

## 🔧 Özellikler

### Web Arayüzü (Streamlit)
- **💬 Interaktif Chat**: Gerçek zamanlı sohbet arayüzü
- **📊 Analytics Dashboard**: Kullanım istatistikleri ve grafikler
- **📁 Veri Görüntüleme**: Veri seti analizi ve görselleştirme
- **⚙️ Model Seçimi**: GPT ve Gemini arasında seçim
- **📤 Dışa Aktarma**: Chat geçmişini JSON/CSV formatında indirme

### Chatbot Yetenekleri
- **🍽️ Yemek Tarifleri**: 20+ klasik Türk yemeği tarifi
- **🛒 Malzeme Listesi**: Detaylı malzeme bilgileri
- **👨‍🍳 Pişirme Teknikleri**: Uzman mutfak ipuçları
- **📊 Beslenme Bilgisi**: Kalori ve besin değeri bilgileri
- **📋 Menü Önerileri**: Farklı durumlar için menü önerileri

### Analitik Özellikler
- **📈 Performans Metrikleri**: Accuracy, Precision, Recall, F1-Score
- **🔄 Model Karşılaştırması**: Farklı modellerin performans analizi
- **📊 Confusion Matrix**: Detaylı hata analizi
- **📉 İnteraktif Grafikler**: Plotly ile dinamik görselleştirmeler

## 🧪 Test Etme

Projenin düzgün çalışıp çalışmadığını kontrol etmek için:

```bash
python test_chatbot.py
```

Bu script şu testleri yapar:
- ✅ Veri seti yükleme
- ✅ Geleneksel ML modeli
- ✅ Veri analizi
- ⚠️ GPT modeli (API anahtarı gerekli)
- ⚠️ Gemini modeli (API anahtarı gerekli)

## 💡 Kullanım Örnekleri

### Temel Sohbet
```
Kullanıcı: "Merhaba"
Bot: "Merhaba! Türk mutfağı hakkında size nasıl yardımcı olabilirim?"

Kullanıcı: "Döner nasıl yapılır?"
Bot: "DÖNER TARİFİ:
🥘 Malzemeler: Et (kuzu/tavuk), Soğan, Domates, Baharat karışımı, Yoğurt, Lavash
👨‍🍳 Yapılışı: 1. Eti ince dilimle. 2. Baharatlarla marine et..."
```

### Malzeme Sorgusu
```
Kullanıcı: "Baklava malzemeleri neler?"
Bot: "BAKLAVA İÇİN GEREKLİ MALZEMELER:
• Yufka
• Ceviz/Fıstık
• Tereyağı
• Şerbet (şeker, su, limon)"
```

### Pişirme Tekniği
```
Kullanıcı: "Et nasıl marine edilir?"
Bot: "🥩 Et marinesi: Yoğurt, limon suyu, zeytinyağı ve baharatları karıştırın. 
Eti en az 2 saat, tercihen gece boyunca bekletin."
```

## 🔧 Teknik Detaylar

- **Intent Classification**: Few-shot learning + Template matching
- **Response Generation**: Rule-based + LLM enhanced
- **API Integration**: OpenAI ve Google AI Studio
- **UI Framework**: Streamlit
- **Data Processing**: Pandas, NumPy, Scikit-learn
- **Visualization**: Plotly, Matplotlib, Seaborn

## 📊 Değerlendirme Metrikleri

### Kullanılan Metrikler:
- **Accuracy**: Doğru sınıflandırma oranı
- **Precision**: Pozitif tahminlerin doğruluk oranı
- **Recall**: Gerçek pozitiflerin yakalanma oranı
- **F1 Score**: Precision ve Recall'un harmonik ortalaması

### Model Seçim Kriterleri:
1. **F1 Score performansı**
2. **Türkçe dil desteği kalitesi**
3. **API maliyet efektifliği**
4. **Response süresi**

## 🚀 Gelecek Geliştirmeler

- [ ] **Multi-turn conversation**: Uzun sohbet geçmişi desteği
- [ ] **Voice interface**: Sesli komut desteği
- [ ] **Recipe recommendations**: Kişiselleştirilmiş tarif önerileri
- [ ] **Image recognition**: Yemek fotoğrafı analizi
- [ ] **Regional cuisine**: Bölgesel mutfak çeşitleri
- [ ] **Nutritional tracking**: Kalori takip sistemi

## ⚡ Hızlı Başlangıç

Sadece test etmek istiyorsanız:

```bash
# 1. Veri setini kontrol edin
python utils/data_preprocessing.py

# 2. Geleneksel ML modelini test edin
python models/intent_classifier.py

# 3. Web arayüzünü başlatın (API anahtarları olmadan da çalışır)
streamlit run app/streamlit_app.py
```

## 🛠️ Sorun Giderme

### Yaygın Sorunlar:

**❌ "Module not found" hatası:**
```bash
pip install -r requirements.txt
```

**❌ "API key not found" hatası:**
- `.env` dosyasının root dizinde olduğundan emin olun
- API anahtarlarının doğru yazıldığından emin olun

**❌ "Excel file not found" hatası:**
```bash
python utils/data_preprocessing.py
```

**❌ Streamlit çalışmıyor:**
```bash
pip install streamlit --upgrade
```

## 📞 Destek

Proje ile ilgili sorularınız için:
- 📧 Email: [email]
- 📚 Documentation: Bu README dosyası
- 🐛 Bug Reports: Issues sekmesi

## 📜 Lisans

Bu proje eğitim amaçlı geliştirilmiştir.

---

**🎉 Projenizi başarıyla tamamladınız! Afiyet olsun! 🍽️** 
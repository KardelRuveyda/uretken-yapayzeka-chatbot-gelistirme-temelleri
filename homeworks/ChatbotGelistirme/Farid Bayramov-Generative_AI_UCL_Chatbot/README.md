# 🏆UEFA Champions League Chatbot

Bu proje, UEFA Şampiyonlar Ligi hakkında kullanıcıların sorularını yanıtlayabilen bir yapay zekâ destekli chatbot geliştirme sürecini kapsamaktadır. Chatbot, kullanıcının niyetini sınıflandırarak (intent classification) uygun yanıtı üretmekte ve yalnızca Şampiyonlar Ligi ile ilgili konulara odaklanmaktadır.

## 🎯 Proje Amacı

- Kullanıcının sorularını analiz ederek niyetini belirlemek.
- Sadece UEFA Şampiyonlar Ligi'ne dair bilgi sağlayan bir chatbot geliştirmek.
- Farklı büyük dil modellerini (LLM) kullanarak chatbot’un çıktısını oluşturmak.
- Kullanılan modellerin performansını karşılaştırmak.

---

## 🚀 Çalıştırma Talimatları

1. **Gereksinimleri Kurun:**

```bash
pip install -r requirements.txt
```
2. **.env Dosyasına api key yazınn:**
```bash
OPENAI_API_KEY=your_openai_key
OPENROUTER_API_KEY=your_openrouter_key
```
3. **Streamlit uygulamasını başlatın:**
```bash
streamlit run app.py
```

## 🧠 Chatbot Akışı

Chatbot aşağıdaki temel niyetlere cevap verebilir:

- `Greeting`: Selamlama (örn. Merhaba)
- `Goodbye`: Vedalaşma (örn. Görüşürüz)
- `Reject`: Reddetme
- `non-champions`: Şampiyonlar Ligi dışı soru algılama
- `Info_*`: Şampiyonlar Ligi hakkında belirli senaryolar (örn. Info_Players, Info_Records vs.)
- `History`: Turnuvanın, takımların tarihi bilgileri
- Ve daha farklı niyet türleriyle birlikte `45` farklı türde niyet sınıfı . . .

### Chatbot Akış Açıklaması

1. Kullanıcıdan metin girişi alınır.
2. Metin `TF-IDF` ile vektörleştirilir ve `SVM` ile intent sınıflandırması yapılır.
3. Eğer niyet Şampiyonlar Ligi ile ilgili değilse, chatbot nazikçe bunu belirtir.
4. Niyet Şampiyonlar Ligi ile ilgiliyse, vektör tabanlı bilgi alma `(RAG)` sistemi ile içerik seçilir.
5. Belirlenen niyet ve bilgi, seçilen LLM'e prompt olarak gönderilir.
6. AI modelinden alınan yanıt kullanıcıya gösterilir.
7. Yanıt üretimi sırasında langchain kütüphanesi ile ChatOpenAI çağrısı yapılır. Prompt içine önce tahmin edilen intent, ardından da vektör tabanlı bilgi dahil edilir. Böylece konu dışına çıkmayan ve bağlama uygun cevaplar üretilir.
---

## 🗃️ Veri Seti

Veri kümesi, `.xlsx` formatında olup `data/champions_league_chatbot_dataset.xlsx` dosyasında yer almaktadır. Veri kümesi aşağıdaki formatta hazırlanmıştır:

| Intent          |                 Example                  |     
|-----------------|------------------------------------------|
| Greeting        | Nice to see you                          | 
| Goodbye         | Until we meet again                      | 
| Tournament_info | Tell me about the champions league.?     |     
|       ...       |             ...                          |                         
|       ...       |             ...                          |                        
|       ...       |             ...                          |           

- Toplam 45 türde intent,  **1195** örnek cümle içerir.
- Veri seti Kaggle link: https://www.kaggle.com/datasets/feridbayramov/champions-league-chatbot-dataset
---

## 🤖 Kullanılan Modeller (LLM)

Projede iki farklı LLM kullanılmıştır:

| Model Adı                                  |        Sağlayıcı     |
|--------------------------------------------|----------------------|
| `GPT-3.5-Turbo`                            |         OPENAI       |
| `qwen/qwen3-235b-a22b:free`                | Alibaba (OpenRouter) |

### Model Seçim Gerekçesi

- **GPT-3.5 Turbo**: Hızlı ve uygun maliyetlidir. Genel amaçlı diyaloglar için güçlüdür ve geniş bir bilgi tabanına sahiptir.
- **Qwen-3 235B**: Büyük kapasitesi ve diyalog becerileri sayesinde detaylı ve doğru cevaplar üretebilir, ücretsizdir.


### Kullanılan API ve Araçlar

- [Platform OPENAI](https://platform.openai.com/api-keys) ve [OpenRouter.ai](https://openrouter.ai) üzerinden API key alındı.
- `openai` Python paketi ile OpenRouter API uyumlu entegrasyon gerçekleştirilmiştir.
- `.env` dosyasından API anahtarı çekilmiştir.


## 🧩 Intent Sınıflandırıcı

- Bu projede kullanıcı sorularını anlamak için `TF-IDF + SVM`
temelli bir niyet sınıflandırıcısı kullanılmıştır.

- `TfidfVectorizer`: N-gram (1,2) ile kelime vektörleri oluşturur.

- `SVC (Support Vector Machine)`: Doğrusal çekirdek (linear kernel) ile sınıflandırma yapar.

- Eğitim sonrası model `models/intent_classifier.pkl` olarak kaydedilir.

- `predict_intent()` fonksiyonu ile gerçek zamanlı tahmin yapılabilir.

- Eğitim/Test oranı: **%70 / %30**

⚠️ Modelin eğitilmesi sırasında maksimum özellik frekansı (max_df=0.95) kullanılmış, İngilizce stopword'ler filtrelenmiştir.

![image](https://github.com/user-attachments/assets/c142d4d9-5202-4e12-98e2-0263db1f1100)


## 🔍 Vektör Tabanlı Bilgi Alma (RAG)

Chatbot'un bilgi kaynağı olarak sadece `data/champions_league_information.txt` dosyası kullanılmaktadır. Bu metin dosyası `CharacterTextSplitter` ile küçük parçalara `(chunk)` ayrılır ve `OpenAIEmbeddings` ile vektörleştirilerek `Chroma` vektör veri tabanına eklenir.

**Kullanılan yapı:**

``CharacterTextSplitter``: `chunk_size=500`, `chunk_overlap=50`

`OpenAIEmbeddings`: `"text-embedding-3-large"` modeli

`Chroma`: Kalıcı veri deposu olarak `"chroma_db"` klasörü kullanılır.

**Bilgi Arama Süreci:**

Kullanıcıdan gelen soru → niyet sınıflandırıcısına gönderilir.

Sınıflandırılan niyet → retriever ile benzer paragraflar alınır.

Alınan bilgi + kullanıcı sorusu → LLM’e prompt olarak iletilir.



## 📊 Model Performans Karşılaştırması
Intent sınıflandırması için `TfidfVectorizer + SVC` pipeline'ı kullanılmıştır. Değerlendirme metrikleri:

- **Precision**
- **Recall**
- **F1 Score**
- **Confusion Matrix** 

### Train/Test Ayrımı

- Eğitim verisi: %70
- Test verisi: %30
- Tüm modeller aynı test seti ile değerlendirilmiştir.

### Performans Sonuçları

| intent               |   precision |   recall |   f1_score |   support |
|:---------------------|------------:|---------:|-----------:|----------:|
| VAR_info             |        1.00 |     1.00 |       1.00 |         7 |
| anthem_info          |        0.71 |     1.00 |       0.83 |         5 |
| assist_leaders       |        1.00 |     1.00 |       1.00 |        12 |
| ball_info            |        1.00 |     1.00 |       1.00 |         9 |
| best_players         |        1.00 |     1.00 |       1.00 |         6 |
| broadcast_info       |        1.00 |     1.00 |       1.00 |         9 |
| champions_history    |        1.00 |     1.00 |       1.00 |         7 |
| clean_sheets         |        0.83 |     1.00 |       0.91 |         5 |
| club_stats           |        1.00 |     0.86 |       0.92 |         7 |
| coach_info           |        1.00 |     1.00 |       1.00 |         9 |
| draw_info            |        1.00 |     1.00 |       1.00 |         5 |
| fan_chants           |        1.00 |     1.00 |       1.00 |         6 |
| final_info           |        1.00 |     1.00 |       1.00 |         7 |
| format_info          |        0.75 |     0.75 |       0.75 |         4 |
| fun_facts            |        1.00 |     0.78 |       0.88 |         9 |
| goodbye              |        1.00 |     0.78 |       0.88 |         9 |
| greeting             |        1.00 |     0.83 |       0.91 |         6 |
| group_standings      |        1.00 |     1.00 |       1.00 |         8 |
| hat_tricks           |        1.00 |     1.00 |       1.00 |        10 |
| history              |        1.00 |     0.73 |       0.84 |        11 |
| injury_news          |        1.00 |     1.00 |       1.00 |         5 |
| knockout_stage       |        1.00 |     1.00 |       1.00 |         9 |
| language_support     |        1.00 |     1.00 |       1.00 |         7 |
| match_result         |        1.00 |     1.00 |       1.00 |         7 |
| match_schedule       |        1.00 |     1.00 |       1.00 |         8 |
| multiple_titles      |        1.00 |     0.89 |       0.94 |         9 |
| non-champions_league |        0.91 |     1.00 |       0.95 |        29 |
| penalty_info         |        1.00 |     1.00 |       1.00 |        13 |
| player_info          |        1.00 |     1.00 |       1.00 |         5 |
| prediction           |        1.00 |     1.00 |       1.00 |         7 |
| ranking              |        1.00 |     1.00 |       1.00 |         6 |
| record_wins          |        1.00 |     1.00 |       1.00 |         7 |
| red_cards            |        0.75 |     1.00 |       0.86 |         6 |
| referee_info         |        1.00 |     1.00 |       1.00 |        10 |
| rules                |        1.00 |     0.88 |       0.93 |         8 |
| sponsorship          |        1.00 |     1.00 |       1.00 |        10 |
| suspensions          |        1.00 |     1.00 |       1.00 |         4 |
| team_info            |        1.00 |     1.00 |       1.00 |         7 |
| team_titles          |        0.80 |     1.00 |       0.89 |         8 |
| tickets_info         |        1.00 |     1.00 |       1.00 |         8 |
| tournament_info      |        0.90 |     0.90 |       0.90 |        10 |
| travel_info          |        1.00 |     1.00 |       1.00 |         9 |
| trophy_info          |        0.89 |     1.00 |       0.94 |         8 |
| venue_info           |        1.00 |     1.00 |       1.00 |         8 |
|`accuracy`          |             |          |       **0.96** |       **359** |          
| `macro avg`            |        **0.97** |     **0.96** |       **0.96** |       **359** |
| `weighted avg`         |        **0.97** |     **0.96** |       **0.96** |       **359** |

---



**Karışıklık matrisi:**

![image](https://github.com/user-attachments/assets/4a5ae4c8-b185-4608-9f60-af1965c2d37c)


---

## 💬 Uygulama Arayüzü

- Gelişmiş bir arayüz olarak `streamlit` destekli görsel arayüz mevcuttur.
- Kullanıcıdan metin alınır ve yanıt ekranda gösterilir.

![image](https://github.com/user-attachments/assets/f6902892-32ae-4c74-b137-0b989461d322)


---

## 📁 Proje Yapısı

```bash
├── data/
│   ├── champions_league_information.txt        #Şampiyonlar Ligi hakkında bilgi metni
│   └── champions_league_chatbot_dataset.xlsx               #Intent sınıflandırma verisi
├── models/
│   └── intent_classifier.pkl                          #Eğitilmiş TF-IDF + SVM modeli
├── app/
│   ├── streamlit_app.py                        # Arayüz için Streamlit uygulaması 
│   ├──  gpt_model.py
│   ├── qwen_model.py                                                   
├── README.md                                    # Proje dökümantasyonu
└── requirements.txt                             # Gerekli Python kütüphaneleri

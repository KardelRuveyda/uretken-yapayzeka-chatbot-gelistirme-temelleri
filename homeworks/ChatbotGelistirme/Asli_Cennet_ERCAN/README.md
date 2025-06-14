# 🤖 ÖSYM Konulu Chatbot Geliştirme Projesi

Bu proje, Ölçme, Seçme ve Yerleştirme Merkezi (ÖSYM) hakkında sık sorulan sorulara yanıt verebilen bir yapay zekâ destekli chatbot sisteminin geliştirilmesini kapsamaktadır. Projede intent (niyet) türlerine dayalı bir veri seti kullanılmış, iki farklı LLM modeline dayalı RAG (Retrieval-Augmented Generation) yapısı uygulanmış ve arayüz olarak Streamlit tercih edilmiştir. Aynı zamanda farklı LLM (Large Language Model) modellerinin karşılaştırılması ve performanslarının değerlendirilmesi amaçlanmıştır.

---

## 👥 Hedef Kitle

* Üniversite adayları ve öğrenciler
* Eğitim danışmanları
* ÖSYM başvuru süreci hakkında bilgi almak isteyen herkes

---

## 👩‍💻 Proje Sahibi

* **Adı Soyadı:** Aslı Cennet Ercan
* **Okul:** Marmara Üniversitesi
* **Bölüm:** Bilgisayar Mühendisliği
* **Ders:** Üretken Yapay Zekâ Chatbot Geliştirme Temelleri
* **Dönem:** Bahar 2025

---

## 🚦 Proje Yapısı

```bash
.
├── data/
│   ├── chatbot_dataset.xlsx          # Intent verileri
│   └── sss.pdf                       # ÖSYM SSS PDF belgesi
├── models/
│   ├── gpt_model.ipynb               # GPT modeliyle RAG
│   └── gemini_model.ipynb            # Gemini modeliyle RAG
├── app/
│   └── streamlit_app.py              # Chatbot uygulama arayüzü
├── requirements.txt                  # Bağımlılıklar
└── README.md                         # Proje tanıtım dosyası
```

---

## 🧠 Chatbot Intent Tasarımı

Chatbot, kullanıcıdan gelen mesajı embed edip intent sınıflandırması yapar. Sonrasında aşağıdaki karar yapısı uygulanır:

* **Selamlama** → "Merhaba! Size nasıl yardımcı olabilirim?"
* **Vedalaşma** → "Görüşmek üzere, başarılar dilerim!"
* **Konu Dışı** → "Bu konuda yardımcı olamıyorum. Lütfen ÖSYM ile ilgili bir soru sorunuz."
* **Diğer (RAG)** → PDF içeriğinden FAISS aracılığıyla bilgi aranır ve cevap üretilir.

> ✔・Intent türleri: `selamlama`, `veda`, `konu_dışı`, `faq_sorgu` (ve diğerleri)

---

## 📂 Veri Seti

### Format

* `chatbot_dataset.xlsx` → 1000+ satır, iki sütun: `Intent` ve `user_message`

### Örnek Satır:

| Intent                    | user\_message                       |
| ------------------------- | ----------------------------------- |
| selamlama                 | Merhaba, yardımcı olabilir misiniz? |
| sinav\_takvimi\_sorgulama | 2025 YKS başvuruları ne zaman?      |

> ✅ Veri, SentenceTransformer kullanılarak embed edilmiştir.

---

## 🗺️ Chatbot Akış Diyagramı

```mermaid
graph TD
    A[ Kullanıcıdan Girdi Al] --> B[ Intent Sınıflandırması Yap]
    B --> C{Intent Türü Nedir?}

    C -->|selamlama| D1[👋 Sabit Selamlama Yanıtı Ver]
    C -->|veda| D2[👋 Sabit Veda Yanıtı Ver]
    C -->|konu_dışı| D3[⚠️ Konu Dışı Uyarısı Ver]
    C -->|faq_sorgu / diğer| E[📄 PDF üzerinden Bilgi Getir (RAG)]

    E --> F{Model Seçimi}
    F -->|Gemini| G1[🤖 Gemini ile Yanıt Üret]
    F -->|GPT-4o| G2[🤖 GPT-4o ile Yanıt Üret]

    D1 --> Z[📜 Yanıt Sohbet Geçmişine Eklenir]
    D2 --> Z
    D3 --> Z
    G1 --> Z
    G2 --> Z

    Z --> H[ Kullanıcıya Yanıt Göster]
```

---

## 🤖 LLM Model Seçimi ve Entegrasyonu

### 🧠 GPT-4o (OpenAI)

* **Neden seçildi?**

  * GPT-4o,  güçlü doğal dil anlama ve üretme kapasitesine sahiptir.
  * Türkçe dilinde oldukça başarılı sonuçlar vermektedir.
  * RAG senaryolarında kısa ve tutarlı yanıtlar üretir.

* **Kullanılan araçlar:**

  * `langchain_openai.ChatOpenAI`
  * Embedding: `OpenAIEmbeddings`

```python
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

* **API entegrasyonu:**

  1. [https://platform.openai.com/](https://platform.openai.com/) → API Key oluşturulur.
  2. `.env` dosyasına `OPENAI_API_KEY=xxx` olarak eklenir.
  3. `load_dotenv()` ile yüklenir.

### 🔷 Gemini 1.5 Flash (Google)

* **Neden seçildi?**

  * Hızlı yanıt üretimi
  * Uzun bağlamlarda yüksek performans
  * Ücretsiz API erişimi (günlük kota dahilinde)

* **Kullanılan araçlar:**

  * `langchain_google_genai.ChatGoogleGenerativeAI`
  * Embedding: `HuggingFaceEmbeddings`

```python
from langchain.embeddings import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
```

* **API entegrasyonu:**

  1. [https://ai.google.dev/gemini-api/docs/api-key](https://ai.google.dev/gemini-api/docs/api-key) → API Key oluşturulur.
  2. `.env` dosyasına `Gemini_API=xxx` olarak eklenir.
  3. `os.getenv("Gemini_API")` ile yüklenir.

---

## 🧠 LLM ve RAG Yapısı

### Prompt Şablonu:

* Sistem promptu: "ÖSYM hakkında uzman bir yardımcı botsun..."
* Kullanıcı girdisi + belge özetleri LLM'e verilir

### Vektör Store:

* `sss.pdf` dosyası `RecursiveCharacterTextSplitter` ile parçalanır
* Embedding yapılır (`OpenAIEmbeddings` veya `HuggingFaceEmbeddings`)
* `FAISS` ile arama yapılır

---

## 📊 Model Performansı Karşılaştırması

### Intent Sınıflandırma (Train(%80)/Test(%20) ayrımı yapılmıştır.)

| Model                 | Precision | Recall | F1 Score | Accuracy |
| --------------------- | --------- | ------ | -------- | -------- |
| Logistic Regression   | 0.97      | 0.98   | 0.97     | 0.98     |


### LLM RAG Yanıtları (Subjektif değerlendirme + BERTScore)

| Model  | Hız    | Doğruluk | Cevap Kalitesi | BERTScore F1 | BERTScore Precision | BERTScore Recall |
| ------ | ------ | -------- | -------------- | ------------ | ------------------- | ---------------- |
| GPT-4o | Yüksek | ✅✅✅✅    | ✅✅✅✅✅          | 0.709        | 0.633               | 0.821            |
| Gemini | Orta   | ✅✅✅✅    | ✅✅✅           | 0.889        | 0.889               | 0.889            |
> ⚠️ Not: Bu testte, belirlenen sorular pipeline üzerinden yanıtlatılmış ve çıktıların tutarlı olması adına sonuçlar manuel olarak eşleştirilmiş referans(kılavuz) metinlerle değerlendirilmiştir.

---

##  Uygulama Arayüzü

* Streamlit ile geliştirilmiştir
* Sidebar: Model seçimi, sohbet temizleme
* Ana alan: Soru kutusu, sohbet geçmişi, yanıt gösterimi
* Enter tuşu veya butonla mesaj gönderimi
* Sohbet geçmişi üstte, yeni sorular altta

---

## 📷 Streamlit Arayüzü 

(→ Aşağıda, chatbot arayüzünün farklı kullanım senaryolarına ait örnek ekran görüntüleri bulunmaktadır.)
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
---

## ⚙️ Kurulum ve Çalıştırma

```bash
# Ortamı oluştur
conda create -n rag_env python=3.10
conda activate rag_env

# Bağımlılıkları yükle
pip install -r requirements.txt

# Streamlit uygulamasını başlat
streamlit run app/streamlit_app.py
```
> ⚠️ Not: Faiss bazı sürümlerle uyumsuzluk gösterdiğinden sanal ortamda Python 3.10 tercih edilmiştir.
---
## ✅ Sonuç

Bu proje, yapay zekâ destekli sistemlerin belge tabanlı bilgiye erişim uygulamasını ve farklı embedding stratejileri ve LLM seçeneklerinin karşılaştırılmasını içermektedir.

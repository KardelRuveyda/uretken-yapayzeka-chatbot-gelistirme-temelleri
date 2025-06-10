![image](https://github.com/user-attachments/assets/173f5b70-9c66-4793-9fa7-5260b1665292)

# 🤖 X Konulu Chatbot Geliştirme Süreci

Bu proje, seçilen bir konuda, yapay zekâ destekli bir chatbot geliştirme sürecini kapsamaktadır. Belirli intent (niyet) türlerine dayalı veri seti hazırlanacak, farklı LLM modelleri ile eğitim gerçekleştirilecek ve performans değerlendirmesi yapılacaktır.

---

## 🚦 Başlangıç

Bu ödev bireysel olarak yapılacaktır. Her öğrenci kendi belirlediği **"X"** konusuna göre chatbot geliştirir.

---

## 🧠 Chatbot Akışı Tasarımı

Chatbot aşağıdaki örnek gibi kullanıcının temel sorularına cevap verebilmelidir:

- Selamlama
- Vedalaşma
- Reddetme
- Sepette ürün işlemleri (ekleme, iade)
- Diğer: Konuya özgü senaryolar

Her chatbot için akış diyagramı veya açıklaması dokümana dahil edilmelidir.

---

## 🗃️ Veri Seti Oluşturma

### 📌 Formatlar:
- `.xlsx` (Excel), `.csv`, `.txt`, `.pdf` dosya formatları kabul edilir.

### 📌 İçerik Gereklilikleri:
- Eğer Intent Classfication gerçekleştiriyorsanız En az **1000 satırlık veri** içermelidir.
- Kullanmayacak iseniz PDF, Word gibi verilerden data okutacaksanız o zaman da az bir veri ile çalışmamalısınız.

- Örnek satır yapısı:

| Intent     | Örnek Cümle                                 |
|------------|---------------------------------------------|
| Greeting   | Merhaba, size nasıl yardımcı olabilirim?    |
| Goodbye    | Görüşmek üzere, iyi günler dilerim.         |


> Not: Veri üretiminde yapay zekâ veya RAG (Retrieval-Augmented Generation) kullanılabilir.

## LLM Model Seçimi ve Eğitimi

Veri seti oluşturulduktan sonra chatbot eğitimi gerçekleştirilmelidir. İki farklı LLM türü seçilmeli ve karşılaştırılmalıdır.

### Örnek Seçim:
- GPT (OpenAI)
- Gemini (Google)

### Açıklanması Gerekenler:
- Neden bu modelleri seçtiğiniz
- Hangi API'leri veya araçları kullandığınız
- OpenAI kullanıyorsanız: API anahtarı alımı ve entegrasyon bilgisi

---

## 📊 Model Performansı Karşılaştırması

Aşağıdaki metriklerle değerlendirme yapılmalıdır:

- Precision
- Recall
- F1 Score
- (İsteğe bağlı) Confusion Matrix

### Train/Test Ayrımı:
- Eğitim ve test verisi ayrı tutulmalı
- Her model aynı veriyle test edilmelidir

### Örnek Karşılaştırma Tablosu:

| Model    | Precision | Recall | F1 Score |
|----------|-----------|--------|----------|
| GPT      | 0.93      | 0.91   | 0.92     |
| Gemini   | 0.91      | 0.92   | 0.91     |

---

## Uygulama Arayüzü

- Chatbot arayüzü örneğin **Streamlit** ile hazırlanabilir.
- Kullanıcıdan girdi alıp çıktıyı göstermelidir.
- Çalışan bir demo veya ekran görüntüsü README’ye eklenmelidir.

---

## Örnek Proje Teslim Yapısı

### GitHub Yapısı:

```bash
├── data/
│   └── chatbot_dataset.xlsx
├── models/
│   ├── gpt_model.py
│   └── gemini_model.py
├── app/
│   └── streamlit_app.py
├── README.md
└── requirements.txt

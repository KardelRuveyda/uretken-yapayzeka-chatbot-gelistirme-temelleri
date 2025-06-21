# 🤖 Yemek Danışmanı Chatbot - GPT & Mistral Tabanlı

Bu proje, **yemek tarifleri** konulu yapay zekâ destekli bir chatbot geliştirme sürecini kapsamaktadır. Chatbot, kullanıcının çeşitli sorularına anlamlı ve doğru yanıtlar verecek şekilde tasarlanmıştır.

---

## 🧠 Chatbot Akışı Tasarımı

Chatbot aşağıdaki temel niyetleri (intent) tanıyacak şekilde tasarlanmıştır:

- **Selamlama (Greeting)**
- **Vedalaşma (Goodbye)**
- **Reddetme (Refuse)**
- **Yemek Danışmanlığına Özgü Diğer Sorular**  
  (örneğin: “Karnıyarık nasıl yapılır?”, “Vegan yemek önerir misin?”, “Elimde patates var ne yapabilirim?”)

### 🔁 Akış Diyagramı / Açıklaması

Chatbot, kullanıcının yazdığı cümleyi embedding yöntemiyle analiz eder, ardından vektör tabanlı arama ile en yakın intent'i belirler.  
Elde edilen intent'in response değeri, büyük dil modeline (LLM) bağlamsal bilgi olarak iletilir. LLM, bu bilgiyi kullanarak kullanıcıya doğal ve anlamlı bir yanıt üretir.

![Akis Diyagrami](https://github.com/sudenurGlcn/YemekChatbot/blob/main/images/AkisDiyagrami.png)
---

## 🗃️ Veri Seti Oluşturma

Bu projede kullanılan veri seti, `.csv` formatında hazırlanmıştır ve 1000’den fazla örnek cümle içermektedir.  
Her satırda bir kullanıcı ifadesi, bu ifadeye karşılık gelen Intent (niyet) ve uygun bir Response (cevap) yer almaktadır. Veri seti, kullanıcının farklı bilgi taleplerini kapsayacak şekilde özenle oluşturulmuştur.

Aşağıda kullanılan Intent kategorileri listelenmiştir:

- Greeting — Kullanıcının selamlaşma ifadeleri  
- Goodbye — Vedalaşma mesajları  
- Thanks — Teşekkür ifadeleri  
- GetRecipe — Belirli bir yemeğin tarifini isteme  
- RecipeByIngredient — Belirli bir malzeme ile tarif sorgulama  
- RecipeByIngredientList — Birden fazla malzemeye göre tarif arama  
- RecipeByCategory — Yemek kategorisine göre tarif sorgulama (ör. tatlılar, çorbalar)  
- RecipeSuggestion — Kullanıcıya tarif önerme  
- RecipeByTime — Hazırlanma süresine göre tarif isteme  
- RecipeDifficulty — Tarifin zorluk derecesini sorma  
- DietFilter — Diyet tipine uygun tarif talebi (ör. vejetaryen, glutensiz)  
- Help — Botun nasıl kullanılacağı hakkında yardım isteme  
- AboutBot — Botun amacı ve yetenekleri hakkında bilgi alma  
- RandomRecipe — Rastgele bir tarif isteme  
- SeasonalRecipe — Mevsime uygun tarif önerisi isteme  
- Reject — Kullanıcının teklifi ya da öneriyi reddetmesi  
- WorldCuisine — Dünya mutfağından tarif isteme (ör. İtalyan, Japon)

| Intent    | Text                            | Response                        |
|-----------|--------------------------------|--------------------------------|
| Greeting  | Merhaba, size nasıl yardımcı olabilirim? | Merhaba! Size nasıl yardımcı olabilirim? |
| Goodbye   | Görüşmek üzere, iyi günler dilerim.      | Hoşça kalın, tekrar bekleriz.   |
| GetRecipe | Karnıyarık nasıl yapılır?                 | Karnıyarık için önce patlıcanları... |

Veri oluşturulurken yapay zekâdan destek alınmıştır (prompt bazlı üretim).

---

## 🤖 Kullanılan Modeller ve Yapılandırmalar

### ✅ Model 1: OpenAI GPT (gpt-3.5-turbo)
- API Sağlayıcı: OpenAI  
- Kullanım Şekli: RESTful API üzerinden doğrudan sorgulama yapılmıştır.  
- Kurulum: openai Python kütüphanesi kullanılarak kolayca entegre edilmiştir.  
- API Anahtarı: `.env` dosyasında güvenli şekilde saklanarak erişim sağlanmıştır.  
- Embedding Yöntemi: `text-embedding-3-large` modeli ile metin vektörleştirme yapılmıştır.  
- Arama Mekanizması: ChromaDB kullanılarak vektör benzerliği ile en yakın içerik seçilmiştir.

---

### ✅ Model 2: NousResearch / Nous-Hermes-2-Mistral-7B-DPO
- Temel Altyapı: Mistral 7B DPO (Direct Preference Optimization)  
- Kullanım Şekli: Hugging Face üzerinden indirilen model, 4-bit quantization ile optimize şekilde yüklenmiştir (BitsAndBytesConfig).  
- Embedding Yöntemi: `sentence-transformers` kütüphanesinden `"paraphrase-multilingual-MiniLM-L12-v2"` modeli ile embedding oluşturulmuştur.  
- Arama Mekanizması: FAISS kütüphanesi kullanılarak `IndexFlatL2` yapısı ile en yakın vektörler tespit edilmiştir.

---

## 🤖 Model Performansı Karşılaştırması

Veri seti %80 eğitim / %20 test olarak ayrılmıştır ve aynı veri seti her iki modelde de test edilmiştir.

### 📊 Karşılaştırmalı Model Performans Tablosu

| Metrik           | OpenAI GPT (gpt-3.5-turbo) | Nous Hermes 2 Mistral |
|------------------|----------------------------|-----------------------|
| **ROUGE-1 (F1)** | 0.8738                     | 0.4599                |
| **ROUGE-2 (F1)** | 0.8019                     | 0.2916                |
| **ROUGE-L (F1)** | 0.8728                     | 0.4177                |
| **BLEU**         | 0.76                       | 0.3111                |
| **BERT Precision** | 0.9645                   | 0.9038                |
| **BERT Recall**    | 0.9602                   | 0.8968                |
| **BERT F1**        | 0.9621                   | 0.9000                |

Yapılan test sonuçları, OpenAI GPT (gpt-3.5-turbo) modelinin genel metin üretim kalitesi açısından Nous Hermes 2 Mistral modeline göre daha yüksek performans gösterdiğini ortaya koymaktadır. Özellikle ROUGE ve BERTScore metriklerinde GPT modeli belirgin üstünlük sağlamıştır.

---

## 💻 Uygulama Arayüzü

LLM modeli olarak OpenAI GPT, elde edilen yüksek doğruluk ve performans sonuçları nedeniyle tercih edilmiştir.  
Chatbot’un kullanıcı arayüzü ise Streamlit kütüphanesi kullanılarak geliştirilmiştir.  

![ChatbotArayüz](https://github.com/sudenurGlcn/YemekChatbot/blob/main/images/Cookish1.jpg)
![ChatbotArayüz](https://github.com/sudenurGlcn/YemekChatbot/blob/main/images/Cookish2.jpg)
### 🚀 Çalıştırma Talimatları

```bash
# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt

# .env dosyasına OpenAI API anahtarınızı ekleyin
# Örnek:
# OPENAI_API_KEY=your_api_key_here

# Uygulamayı başlatın
streamlit run app.py
```
---
##🛠️ Kullanılan Kütüphaneler ve Teknolojiler
-	langchain_community
-	langchain_text_splitters
-	langchain_openai
-	langchain_core
-	langchain
-	python-dotenv
-	pandas
-	faiss-cpu
-	pickle
-	sentence-transformers
-	transformers
-	torch

## Chatbotlar neden hatalı cevaplar verir?

**Kullanıcı chatbot’a şu soruyu soruyor:**

_“Sağlık poliçem kalça ultrasonunu kapsıyor mu?”_

**Botun cevabı:**

_“Üzülerek söylemeliyim ki Zorunlu Trafik Sigortası yurt dışında geçerli değildir.”_

**Burada ciddi bir bağlam hatası var:**

* Kullanıcı “sağlık sigortası” hakkında bir soru soruyor.
* Bot ise “trafik sigortası” hakkında bir cevap veriyor.

![image](https://github.com/user-attachments/assets/c015b90c-59b2-4141-8f72-8fb6cc62b61a)


## Teori 1 Klasik Makine Öğrenmesi (ML) ile Geliştirilmiş Bot

* Bu tarz botlar genellikle sabit sınıflandırmalara ve sınırlı veri kümelerine dayanır.
* Eğitim verisi yetersiz veya bağlam algısı zayıf olabilir.
* Cümlede geçen “**poliçe**” kelimesi botu yanlış sınıfa yönlendirmiş olabilir.

**✅ İhtimal: Yüksek**
* Çünkü klasik botlar genellikle bağlamı güçlü analiz edemez ve yüzeysel eşleşmeye göre cevap verir.

### 🧩 Intent Temelli Tasarım Nedir?

Chatbot’un temelinde, kullanıcının niyetini anlamaya yönelik bir yapı kurulur. Bu yapılara “Intent” (Niyet) denir.

**Örneğin:**

- “Naber nasılsın?” → Selamlama (Greeting)
- “Poliçe oluşturmak istiyorum.” → Poliçe Oluşturma

### 🧠 Intent Türleri

_**Diyagramda 2 tür intent tanımlanmış:**_

**Dialog Intentleri:** Sohbet akışını yöneten niyetler

- Selamlama
- Vedalaşma
- Onaylama
- Reddetme

**Bilgi İçeren Bot Intentleri:** Kullanıcının bilgi veya işlem talebi

- Trafik Sigortası
- Sağlık Sigortası
- Poliçe Oluşturma
- Teklif Oluşturma

💡 **Toplam**: 8 kategoriye ayrılmış 22 örnek veri seti var.

### 💬 Veri Toplama ve Eğitim Hazırlığı

Kullanıcı örnek cümleler yazarak her intent için örnek veri üretir. Örnek:

- **Selamlama**: “Selaminko”, “Nasılsın”, “Naber”
- **Reddetme**: “İstemem”, “Hayır”, “Olmasın”
- **Trafik Sigortası**: “Trafik sigortası nasıl yaptırırım?” vb.

Her intent sınıfı için **1–4** arası örnek cümle üretilmiş.

### Model Eğitimi Süreci 🧪

Model, bu veri kümeleriyle eğitiliyor.
Eğitimde kullanılan teknikler:

- Word2Vec, Glove, FastText gibi gömme (embedding) yöntemleri
- İhtiyaca göre fine-tune edilmiş büyük bir dil modeli de olabilir

### 🔁 Veri Ayrımı ve Değerlendirme

**Veriler 2’ye ayrılıyor:**

* %80 Eğitim Verisi (17.6 örnek)
* %20 Test Verisi (4.4 örnek)

**Bu veri ile model:**

* Intent Classification görevini öğreniyor.
* Test verisiyle modeli “gerçek dünya” koşullarında test ediyorsunuz.

**⚠️ Dikkat! Eğer model eğitim verisinde çok başarılı ama testte başarısızsa bu overfitting (aşırı öğrenme) problemidir.**

### 🔍 Neden Bu Süreçte Hata Olabilir?

**Bu yapı:**

* Sabit sayıda örnekle çalışır (veri azsa performans düşer)
* Bağlam anlayışı yoktur (kelime eşleşmesiyle sınırlıdır)
* Eğitilmemiş bir intent (örneğin sağlık poliçesi) girilirse yanlış sınıfa atanabilir

_**🧨 Sonuç: Sağlık sigortası sorulmasına rağmen “trafik sigortası” gibi alakasız cevaplar verilebilir. Bu da ilk paylaştığın görseldeki hatalı cevap örneğini açıklar.**_

![image](https://github.com/user-attachments/assets/b6d01fd7-095b-47fe-8ae2-a5136b4b4014)

![image](https://github.com/user-attachments/assets/3f5fc986-85f6-40f4-879c-a145538ea25b)



## Teori 2 LLM + RAG Kullanılmış Ancak Halüsinasyon Olmuş

* Eğer bot, LLM ve RAG destekliyse (örneğin GPT tabanlı), veritabanı ya da bilgi kaynağından gelen yanıtı üretim sürecinde yanlış ilişkilendirmiş olabilir.
* Bu durumda “hallucination” yani LLM’in uydurma cevap verme durumu söz konusu olabilir.

**❗️İhtimal: Düşük**
* Çünkü LLM’ler genellikle bağlamı çok daha iyi anlar. Ancak doğru yapılandırılmaz veya yanlış veriyle desteklenirse bu tür hatalar yine de olabilir.

### 🔢 Adım 1 - Veri Seti Hazırlığı (Text Verisi)

- Chatbot için diyaloğa dayalı veya bilgi temelli soruların yer aldığı veri seti hazırlanır.
- Örnek:
  - **Soru:** “Sağlık poliçem kalça ultrasonunu kapsıyor mu?”
  - Bu tür sorular farklı kategorilerde etiketlenebilir (sağlık, trafik, onay, selamlama vs.)

### 🧠 Adım 2 - LLM Seçimi

- Generative AI destekli bir sistemde büyük dil modelleri (LLM'ler) kullanılır.
- Model şirket içinde eğitilmiş (on-premise) olabilir ya da bir cloud servisinden alınmış olabilir.

### 🔁 Adım 3 - Embedding ve Vektör Veritabanı

- Elimizdeki **metin verisi**, LLM’in anlayabilmesi için **vektör** (embedding) formatına çevrilir.
- Bu vektörler, ChromaDB, Faiss gibi vektör veritabanlarında saklanır.

### ⚙️ Adım 4 - Prompt Mühendisliği

- LLM’e giden prompt’lar doğru tanımlanmalıdır.
- Örneğin:
  > “Sen yalnızca sigorta poliçeleri hakkında bilgi veren bir asistansın. Diğer konulara yanıt vermemelisin.”

- Temperature, Top-p gibi parametreler de dikkatle ayarlanmalı, aksi halde **LLM halüsinasyon riski** taşır.


### 🔄 RAG (Retriever-Augmented Generation) Süreci

1. **Kullanıcının sorusu** vektöre çevrilir.
2. Vektör veritabanında en benzer içerikler bulunur.
3. Bu belgeler LLM’e **destek veri** olarak gönderilir.
4. LLM prompt + belge içeriklerine göre yanıt üretir.


### 🚨 3. Hatalı Cevap Durumu: Ne Oldu?

**❓ Soru**:

> “Sağlık poliçem kalça ultrasonunu kapsıyor mu?”

**❌ Yanıt:**

> “Üzülerek söylemeliyim ki Zorunlu Trafik Sigortası yurt dışında geçerli değildir.”

### 📉 Neden Bu Yanıt Geldi?

- **Olası Sebep 1:** Trafik Sigortasıyla ilgili dökümanlar vektör veritabanında daha fazla olabilir. En yakın belge bu kategoriye ait olabilir.
- **Olası Sebep 2:** Prompt net değilse ya da temperature değeri yüksekse, model doğru dokümantasyona rağmen **halüsinasyon** üretmiş olabilir.


RAG mimarisinde doğru döküman, doğru embedding ve doğru prompt olmazsa:

- LLM yanlış bilgiyle eğitilir.
- Kullanıcı sorusuna yanlış yanıt döner.
- Sistem güvenilirliğini kaybedebilir.


| Aşama              | Risk                                                   |
|--------------------|--------------------------------------------------------|
| Veri Hazırlığı     | Eksik veya dengesiz veri → yanlış yakınlık            |
| Embedding          | Kalitesiz vektörler → alakasız sonuçlar               |
| Prompt Mühendisliği| Eksik yönlendirme → kontrolsüz model davranışı        |
| Temperature        | Yüksek değer → halüsinasyon riski                     |

---

![image](https://github.com/user-attachments/assets/ad34c386-2997-4557-8e7f-d2f26d644982)
![image](https://github.com/user-attachments/assets/ea43d832-2261-4150-af45-f6f2b159c6e6)
![image](https://github.com/user-attachments/assets/1a661098-66a9-4522-a3f9-94d42acfaff5)


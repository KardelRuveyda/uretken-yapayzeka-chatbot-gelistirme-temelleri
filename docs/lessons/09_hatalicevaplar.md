## Chatbotlar neden hatalı cevaplar verir?

**Kullanıcı chatbot’a şu soruyu soruyor:**

_“Sağlık poliçem kalça ultrasonunu kapsıyor mu?”_

**Botun cevabı:**

_“Üzülerek söylemeliyim ki Zorunlu Trafik Sigortası yurt dışında geçerli değildir.”_

**Burada ciddi bir bağlam hatası var:**

* Kullanıcı “sağlık sigortası” hakkında bir soru soruyor.
* Bot ise “trafik sigortası” hakkında bir cevap veriyor.

![image](https://github.com/user-attachments/assets/c015b90c-59b2-4141-8f72-8fb6cc62b61a)


## Teori 1

### 🎯 TEORİ 1 – Klasik Makine Öğrenmesi (ML) ile Geliştirilmiş Bot

* Bu tarz botlar genellikle sabit sınıflandırmalara ve sınırlı veri kümelerine dayanır.
* Eğitim verisi yetersiz veya bağlam algısı zayıf olabilir.
* Cümlede geçen “**poliçe**” kelimesi botu yanlış sınıfa yönlendirmiş olabilir.

**✅ İhtimal: Yüksek**
* Çünkü klasik botlar genellikle bağlamı güçlü analiz edemez ve yüzeysel eşleşmeye göre cevap verir.

![image](https://github.com/user-attachments/assets/b6d01fd7-095b-47fe-8ae2-a5136b4b4014)

## Teori 1 Gerçekleşme Süreci 

![image](https://github.com/user-attachments/assets/3f5fc986-85f6-40f4-879c-a145538ea25b)



## Teori 2

### 🤖 LLM + RAG Kullanılmış Ancak Halüsinasyon Olmuş

* Eğer bot, LLM ve RAG destekliyse (örneğin GPT tabanlı), veritabanı ya da bilgi kaynağından gelen yanıtı üretim sürecinde yanlış ilişkilendirmiş olabilir.
* Bu durumda “hallucination” yani LLM’in uydurma cevap verme durumu söz konusu olabilir.

**❗️İhtimal: Düşük**
* Çünkü LLM’ler genellikle bağlamı çok daha iyi anlar. Ancak doğru yapılandırılmaz veya yanlış veriyle desteklenirse bu tür hatalar yine de olabilir.

![image](https://github.com/user-attachments/assets/ad34c386-2997-4557-8e7f-d2f26d644982)


![image](https://github.com/user-attachments/assets/ea43d832-2261-4150-af45-f6f2b159c6e6)


## Teori 2 Gerçekleşme Süreci

![image](https://github.com/user-attachments/assets/1a661098-66a9-4522-a3f9-94d42acfaff5)


# 🧠 Chatbot Akışı Tasarımı

![Chatbot Akış Diyagramı](homeworks\marmara\Elif_Tilki\chatbot_homework_elif_tilki\images\diagram.png)  
*Yukarıdaki diyagram, chatbotun temel çalışma prensibini ve kullanıcı ile etkileşim sürecini görsel olarak özetlemektedir.*

Chatbot, kullanıcıdan aldığı girdiyi işleyerek anlamlandırmakta ve buna uygun yanıtları üretmektedir.

Akış şu şekilde işlemektedir:  
Öncelikle sistem başlatılır ve kullanıcıdan bir giriş alınır. Kullanıcının yazdığı cümle, doğal dil işleme için tokenizer kullanılarak parçalara ayrılır. Ardından, BERT ya da T5 tabanlı bir model ile kullanıcının niyeti (intent) tahmin edilir. Bu tahmin, önceden tanımlanmış intent listesinde kontrol edilir. Eğer tahmin edilen intent listede varsa, bu niyete karşılık gelen cevaplar Excel dosyasından yüklenir ve aralarından rastgele bir yanıt seçilerek kullanıcıya gösterilir. Eğer intent listede yoksa, chatbot önceden belirlenmiş genel bir fallback (geri dönüş) cevabı ile kullanıcının sorusuna yanıt verir.

## 📂 Veri Seti Açıklaması

Bu projede geliştirilen chatbot, **kitap önerisi** konulu kullanıcı isteklerini anlayarak uygun yanıtlar üretmektedir. Chatbot’un eğitimi ve değerlendirmesi için özel olarak hazırlanmış bir veri seti kullanılmıştır.

---

### 🔍 Veri Setinin Amacı

Amaç, kullanıcıdan gelen doğal dil ifadelerini sınıflandırarak, bunlara uygun kitap türü/tavsiyesi belirlemek ve buna göre yanıt üretmektir. Bu doğrultuda, **Intent Classification** yaklaşımı kullanılmıştır.

---

### 📄 Veri Formatı ve İçeriği

Veri seti `.xlsx` formatında hazırlanmış olup, her satırda bir örnek kullanıcı cümlesi ve buna karşılık gelen bir *intent (niyet)* etiketi bulunmaktadır.
Bu projede toplam 24 farklı intent etiketi kullanılmıştır. Her intentte 50 tane örnek bulunmaktadır. Bu intentler arasında kitap türlerine yönelik isteklerin yanı sıra sohbet (greeting, goodbye) ve bilinmeyen istekler için özel intentler de yer almaktadır:

**veri yapısı:**

| Intent | Example |
|--------|--------|
| request_science_fiction_books | bilim kurgu klasiklerinden birkaç kitap önerebilir misin |
| request_fantasy_books | fantastik evrenlerde geçen kitaplar arıyorum |
| request_historical_books | tarihi olayları konu alan kitapları severim, ne önerirsin |
| request_detective_mystery_books | polisiye ve dedektiflik içeren romanları seviyorum, ne önerirsin |
| request_horror_books | korku ve gerilim unsurları barındıran kitaplar önerir misin |
| request_romance_books | klasik aşk romanları önerir misin |
| request_biography_books | biyografi türünde etkileyici kitaplar var mı |
| request_poetry_books | duygusal şiirleri içeren kitaplar var mı |
| request_theater_books | tiyatro üzerine kısa oyun metinleri içeren kitaplar arıyorum |
| request_comic_books | popüler çizgi roman serileri nelerdir |
| request_food_books | gourmet yemek tarifleri içeren kitaplar var mı |
| request_chess_books | stratejik satranç oyun planları hakkında kitaplar arıyorum |
| request_classic_books | klasik edebiyatın başyapıtları hangileridir |
| request_bestselling_books | bestseller listesinde hangi kitaplar var |
| request_self_improvement_books | kişisel gelişimle ilgili etkili kitap önerileri alabilir miyim |
| request_motivational_books | kendimi motive etmek için okuyabileceğim kitaplar hangileri |
| request_philosophical_books | felsefi akımlar ve düşünürler üzerine kapsamlı kitaplar arıyorum |
| request_adventure_books | macera dolu hikayeler içeren kitaplar arıyorum |
| request_educational_books | eğitimle ilgili yeni çıkan kitaplar nelerdir |
| request_short_story_books | kısa hikaye türünde en çok okunan kitaplar hangileri |
| request_kids_books | küçük yaş grupları için kitap önerileri verir misin |
| conversation_greeting | Merhaba, kitap önerisi alabilir miyim?   |
| conversation_goodbye | Teşekkürler, hoşça kal   |
| fallback_unknown_request | Şu an saat kaç |

- `request_...`: Belirli kitap türlerine yönelik kullanıcı isteklerini temsil eder.

- `conversation_...`: Sohbetin doğal akışını sağlayan selamlaşma/vedalaşma niyetleridir.

- `fallback_unknown_request`: Anlaşılmayan kullanıcı ifadeleri için kullanılır.

Veri seti toplamda 1200 örnek cümle içermektedir. Veri seti oluşturulurken farklı kitap türlerine yönelik çeşitli kullanıcı ifadeleri türetilmiştir. Verinin üretiminde, içerik çeşitliliğini sağlamak amacıyla **yapay zekâ destekli otomatik veri üretim yöntemlerinden** yararlanılmıştır (örneğin: LLM tabanlı jenerasyon).

---

### ✂️ Train/Test Ayrımı

Modelin eğitimi ve doğrulaması sırasında **veri kaçağını (data leakage)** önlemek adına veri seti eğitim ve test olarak ayrılmıştır. Bölme işlemi yapılırken sınıf dağılımının korunması için **Stratified Split** yöntemi tercih edilmiştir.

Bu ayrım sonucunda:

- **Eğitim (Train) seti:** 960 örnek (yani toplam verinin %80’i)  
- **Test seti:** 240 örnek (toplam verinin %20’si)

**Kullanılan Python kodu:**

```python
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_excel("book_recommendation_dataset_3.xlsx")
X = df['Example']
y = df['Intent']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

train_df = pd.DataFrame({'Example': X_train, 'Intent': y_train})
test_df = pd.DataFrame({'Example': X_test, 'Intent': y_test})

train_df.to_excel("train.xlsx", index=False)
test_df.to_excel("test.xlsx", index=False)
```
Bu kod sayesinde veriler `train.xlsx` ve `test.xlsx` olarak iki ayrı dosyada saklanmıştır.

---

### 💬 Intent-Cevap Eşleştirmesi

Modelin sadece doğru intent’i tahmin etmesi değil, aynı zamanda **anlamlı ve çeşitli yanıtlar vermesi** hedeflenmiştir. Bu nedenle `intent_cevaplari.xlsx` adında bir yardımcı dosya hazırlanmıştır.

Her bir intent için **beş farklı yanıt** oluşturulmuş, böylece chatbot’un daha **dinamik** ve **zengin** yanıtlar üretebilmesi sağlanmıştır.

**Örnek yapı:**

| Intent | Cevap1 | Cevap2 | Cevap3 | Cevap4 | Cevap5 |
|--------|--------|--------|--------|--------|--------|
| request_science_fiction_books | Bilim kurgu dünyasının klasikleri arasında yer alan Isaac Asimov’un "Vakıf" serisi... | ... | ... | ... | ... |

Yanıtlar, ilgili kitap türüne dair öneriler sunacak şekilde **çeşitlendirilmiş** ve farklı kullanıcı profillerine hitap edebilecek şekilde hazırlanmıştır.  

---

### 🧠 Özet

- ✅ Veri seti toplamda 1200 örnek cümle içermektedir.
- ✅ Veri, 24 farklı intent etiketini kapsamaktadır.
- ✅ Veriler `.xlsx` formatında düzenlenmiş, **eğitim ve test ayrımı** yapılmıştır.
- ✅ Ek olarak, chatbot’un yanıt üretmesi için **intent-yanıt eşleşme tablosu** oluşturulmuştur.
- ✅ Veri seti, projenin hem **eğitimi** hem de **performans değerlendirmesi** aşamalarında kullanılmıştır.

# 🧠 Model Seçimi ve Eğitimi

Bu projede iki farklı Transformer tabanlı dil modeli kullanılarak chatbot amaçlı intent sınıflandırması gerçekleştirilmiştir: **BERT** ve **T5**. Bu modeller, doğal dil işleme alanında başarılı performansları ile bilinir ve farklı çalışma prensiplerine sahiptir.

---

## 1. BERT (Bidirectional Encoder Representations from Transformers)

- **Model**: `bert-base-uncased`  
- **Kütüphaneler**: Hugging Face Transformers, PyTorch  

### 🔍 Çalışma Prensibi

BERT, çift yönlü bir encoder modelidir. Girdi metnini anlamak için tüm bağlamı aynı anda değerlendirir. Bu projede intent sınıflandırma için son katmanı fine-tune edilerek kullanılmıştır.

### 🛠️ Veri İşleme

- Tokenizer ile metinler tokenize edildi  
- Pad/Padding uygulandı  
- Label mapping yapıldı  

### ⚙️ Eğitim Detayları

- **Eğitim Ortamı**: Google Colab Pro, NVIDIA L4 GPU  
- **Epoch Sayısı**: 50 
- **Çalışan Epoch Sayısı**: 17 (erken durdurma ile) 
- **Eğitim Süresi**: Yaklaşık 4 dakika  
- **Batch Size**: 16  
- **Learning Rate**: 2e-5  
- **Erken Durdurma**: Kullanıldı
- 
### ✅ Avantajlar

- Sınıflandırma görevlerinde yüksek doğruluk  
- Stabil sonuçlar  

### 📉 Confusion Matrix - BERT

![BERT Confusion Matrix](homeworks\ChatbotGelistirme\elif_tilki\images\bert_conf_matrix.png)

---

## 2. T5 (Text-to-Text Transfer Transformer)

- **Model**: `google/flan-t5-base`  
- **Kütüphaneler**: Hugging Face Transformers, PyTorch  

### 🔍 Çalışma Prensibi

T5, metni metne çeviren bir modeldir. Intent sınıflandırma için giriş `"classify intent: <metin>"` formatında verilir, model de doğrudan intent etiketini üretir.

### 🛠️ Veri İşleme

- Girdi ve çıktı metinleri tokenizer ile uygun uzunlukta tokenize edildi  
- Padding uygulandı  
- Output label'lar için `-100` maskesi kullanıldı  

### ⚙️ Eğitim Detayları

- **Eğitim Ortamı**: Google Colab Pro, NVIDIA L4 GPU  
- **Epoch Sayısı**: 50
- **Çalışan Epoch Sayısı**: 43 (erken durdurma ile)  
- **Eğitim Süresi**: Yaklaşık 17 dakika  
- **Batch Size**: 16  
- **Learning Rate**: 2e-5  
- **Erken Durdurma**: Kullanıldı  

### ✅ Avantajlar

- Daha esnek metin üretimi  
- Farklı görevlerde yeniden kullanılabilirlik  

### 📉 Confusion Matrix - T5

![T5 Confusion Matrix](homeworks\ChatbotGelistirme\elif_tilki\images\t5_conf_matrix.png) 

---

## 🔍 Karşılaştırma ve Değerlendirme

| Model | Precision | Recall | F1 Score |Accuracy| 
|-------|-----------|--------|----------|--------|
| BERT  | 0.9495    | 0.9458 | 0.9450   | 0.95   | 
| T5    | 0.8683    | 0.8538 | 0.8547   | 0.93   |

Her iki model de aynı eğitim ve test verisiyle karşılaştırılmıştır. Performans metriği olarak **Precision**, **Recall** ve **F1 Score** dikkate alınmıştır. 
Adil bir karşılaştırma yapılabilmesi için her iki modelde de aynı batch size (16) ve aynı learning rate (2e-5) kullanılmıştır. Epoch sayısı, erken durdurma kriterlerine bağlı olarak farklılık göstermektedir.
**BERT** modeli biraz daha yüksek başarı gösterirken, **T5** modelinin esnekliği ve text-to-text yapısı farklı kullanım senaryoları için avantaj sağlamaktadır.

### Genel Performans

**BERT** modeli, tüm metriklerde **T5** modelinden daha yüksek skorlar elde etmiştir. Özellikle:

- **Precision (Doğruluk):**  
  BERT, daha az yanlış pozitif tahmin yaparak **%95**'e yakın bir doğruluk sağlamıştır.

- **Recall (Duyarlılık):**  
  Gerçek sınıfları bulmadaki başarısı da BERT’te daha yüksektir. Bu da chatbot’un kullanıcı niyetlerini kaçırma oranının daha düşük olduğu anlamına gelir.

- **F1 Score:**  
  Hem precision hem recall’u dengeleyen bu metrikte de BERT **%94.5** ile öne çıkmaktadır.

- **Accuracy:**  
  Genel doğru tahmin oranı BERT için **%95**, T5 için **%93**’tür.


### Detaylı Gözlemler

- **T5** modelinde bazı sınıflar hiç temsil edilmemiştir (`support = 0`).  
  Bu durum, modelin bu sınıflarla ilgili yeterli eğitilmediğini ya da çıktılarının sınıflandırma açısından eksik kaldığını göstermektedir.

- Her iki modelde de `"request_fantasy_books"` ve `"request_science_fiction_books"` gibi bazı sınıflarda **recall oranı** diğerlerine kıyasla daha düşüktür.  
  Bu durum, bu tür cümlelerin model tarafından daha karmaşık veya örtük bulunabileceğini düşündürebilir.


### Sonuç ve Öneri

Bu değerlendirme, **BERT** tabanlı modelin kitap öneri chatbotu uygulaması için daha **uygun ve güvenilir** bir seçim olduğunu göstermektedir.

- Doğru sınıflandırma oranı daha yüksektir.
- Yanlış pozitif/negatif oranları daha düşüktür.

**T5**, daha yaratıcı ve jeneratif görevlerde başarılı bir model olsa da, bu görevde sınıflandırma kabiliyetinde BERT’e kıyasla geri planda kalmıştır.  

---

## ⚙️ Eğitim Süreci ve Araçlar

- **API ve Araçlar**: Hugging Face Transformers, PyTorch  
- **Donanım**: Google Colab Pro, NVIDIA L4 GPU  
- **Model Kaydetme**: Ağırlıklar ve label-id eşlemeleri eğitim sonunda kaydedildi  
- **Erken Durdurma**: Overfitting’i önlemek için kullanıldı  

## 🖥️ Uygulama Arayüzü

Chatbot sistemine kullanıcı etkileşimi kazandırmak amacıyla **Streamlit** tabanlı bir web arayüzü geliştirilmiştir. Bu arayüz sayesinde kullanıcılar, doğal dilde kitap önerisi taleplerini yazabilir ve chatbot’un gerçek zamanlı yanıtlarını görüntüleyebilirler.

---

## ⚙️ Arayüzün Temel Özellikleri

- Kullanıcıdan serbest metin girişi alınır.
- Kullanıcı, iki modelden birini (**BERT** veya **T5**) seçebilir.
- Seçilen model, girdiye uygun intent'i (niyeti) sınıflandırır.
- Belirlenen intent’e uygun, önceden tanımlanmış cevaplardan rastgele biri kullanıcıya gösterilir.
- Hangi niyetin sınıflandırıldığı kullanıcıya açıklanır (🎯 **Niyet: ...**).
- Sayfa tasarımı, kullanıcı deneyimini artırmak için özel CSS ile özelleştirilmiştir.

---

## 📁 Kullanılan Dosyalar ve Gereksinimler

Arayüzün sağlıklı çalışabilmesi için aşağıdaki dosya ve dizinlerin proje yapısında doğru şekilde konumlandırılması gerekmektedir:

| Dosya / Dizin         | Açıklama                                                                 |
|------------------------|--------------------------------------------------------------------------|
| `streamlit_app.py`     | Streamlit tabanlı arayüzü çalıştıran ana dosya.                         |
| `./bert_output/`       | Eğitilmiş BERT modelinin ağırlıklarını içerir.                          |
| `./best_t5_model/`     | Eğitilmiş T5 modelinin ağırlıklarını içerir.                            |
| `intent_cevaplari.xlsx`| Her intent için farklı cevapları içeren Excel dosyası.                  |
| `label2id.pkl`         | BERT modeline özel intent-id eşlemesini içeren pickle dosyası.          |

---

## 🧪 Model Seçimi Özelliği

Arayüzde kullanıcıya `"BERT"` veya `"T5"` modellerinden birini seçme imkânı sunulmuştur. Seçilen modele göre uygun chatbot sınıfı yüklenir ve cevaplama süreci bu modele göre çalışır.  
Ayrıca, **Streamlit**’in `@st.cache_resource` dekoratörü sayesinde model sadece bir kez yüklenir, böylece sistem performansı optimize edilir.

---

## 📥 Kullanım Örneği

Arayüzü başlatmak için terminalde aşağıdaki komut çalıştırılmalıdır:

```bash
streamlit run streamlit_chatbot_app.py
```
Açılan web arayüzünde:

1. **Model seçilir** (`BERT` veya `T5`)
2. Aşağıdaki gibi bir mesaj yazılır:

    ```text
    Macera dolu bir kitap önerir misin?
    ```

3. Model, bu girdi üzerinden ilgili intent’i (örneğin `Adventure`) tanımlar ve uygun cevabı üretir.
4. Sohbet ekranında hem yanıt hem de sınıflandırılan niyet aşağıdaki şekilde görüntülenir:

    ```text
    Yanıt: Jules Verne’in Denizler Altında Yirmi Bin Fersah kitabı, denizaltı maceralarını sevenler için heyecan dolu ve sürükleyici bir klasik olarak önerilir.
    🎯 Niyet: request_adventure_books
    ```

---

## 📸 Ekran Görüntüleri

Aşağıda uygulamanın farklı kullanım senaryolarına ait örnek ekran görüntüleri sunulmuştur:

- 🎨 **Genel Arayüz Görünümü**  
  ![Genel Arayüz](homeworks\ChatbotGelistirme\elif_tilki\images\arayuz_genel.PNG)

- 🤖 **BERT Modeli ile Sohbet**  
  ![BERT Sohbet](homeworks\ChatbotGelistirme\elif_tilki\images\bert_sohbet.PNG)

- 🤖 **T5 Modeli ile Sohbet**  
  ![T5 Sohbet](homeworks\ChatbotGelistirme\elif_tilki\images\t5_sohbet.PNG)



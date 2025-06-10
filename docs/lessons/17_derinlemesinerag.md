# Retrieval-Augmented Generation (RAG): Temelden İleri Düzeye Ders Dokümanı

## 1. Giriş

### RAG Nedir?
Retrieval-Augmented Generation (RAG), büyük dil modellerinin (LLM) dış bilgi kaynaklarını kullanarak
metin üretmesini sağlayan bir yapay zeka mimarisidir. Kısaca, bir LLM’e entegre edilen bilgi getirme
(retrieval) mekanizması sayesinde model, yanıt üretirken eğitim verilerinin ötesindeki güncel ve güvenilir
bilgilere erişebilir . Bu teknik ile model çıktıları kanıtlara dayalı hale gelir ve daha isabetli olur. RAG
yaklaşımı, doğal dil işleme alanında bilgi çekme (retrieval) ve metin üretimi (generation) yeteneklerini tek bir
çatı altında birleştirir; böylece modeller daha derin ve bilgi odaklı cevaplar üretebilir

### Neden Önemlidir?
Geleneksel büyük dil modelleri eğitim aldıkları veriyle sınırlıdır ve zamanla bilgilerinin güncelliğini yitirir. Bu
modeller, parametrelerine “gömülü” olmayan yeni bilgiler karşısında halüsinasyon diyebileceğimiz
uydurma cevaplar verebilir. RAG, LLM’lerin güncel ve doğrulanabilir bilgiye erişimini sağlayarak bu
sorunları giderir. Temel modeli yeniden eğitmeye gerek kalmadan, modele harici veri kaynaklarından
hedeflenmiş bilgiler sunulur; model de bu sayede bağlama uygun, tutarlı ve güncel yanıtlar oluşturabilir. Sonuç olarak RAG, LLM’lerin tek başına yapabildiklerinin ötesine geçip yanıt kalitesini artırır ve hatalı
çıkarımları azaltır.  Ayrıca, RAG yaklaşımı sayesinde bir modelin bilgi tabanı istenildiği zaman
güncellenebildiğinden, modeli yeniden eğitmenin yüksek maliyetinden kaçınılır.


### Kullanım Alanları

RAG mimarisi, geniş bir uygulama yelpazesinde kullanılır. Aşağıda bazı önemli kullanım alanları yer
almaktadır:

- **Soru-Cevap ve Arama Motorları** 
RAG, arama motorları ve açık uçlu soru-cevap sistemlerinde
güncel bilgiye dayalı cevaplar vermek için idealdir. Örneğin, Bing gibi modern arama asistanları,
web’den ilgili içerikleri getirip dil modeli ile cevabı derleyerek kullanıcılara sunar (bu da bir RAG
uygulamasıdır)
- **Müşteri Desteği Chatbotları**
Şirketler, ürün ve hizmet bilgilerini içeren bilgi tabanlarını LLM’lere
entegre ederek müşteri sorularına doğru yanıtlar verir. OpenAI’nin ChatGPT modelinin knowledge
retrieval özelliği ile destek ekibi botlarının, geçmiş destek kayıtlarını sorgulayıp güncel ve şirket-özel
cevaplar üretmesi buna örnek verilebilir.

- **Kişisel Asistanlar**
Kişisel dokümanlar, e-postalar veya notlar üzerinde çalışan yapay zeka asistanları
RAG’den faydalanır. Örneğin, Notion’ın Ask AI özelliği ya da Microsoft’un Copilot sistemi, kullanıcının
kendi verilerinden arama yaparak soruları yanıtlar ve belge özetleme gibi işlemleri gerçekleştirir.
- **İçerik Öneri Sistemleri**
RAG, geleneksel olarak karmaşık model kombinasyonları gerektiren içerik
tavsiye problemlerini basitleştirebilir. Bir LLM’in genel bilgisini, kullanıcının özel tercih verileriyle
birleştirerek kişiselleştirilmiş öneriler oluşturmak mümkündür.
- **Kurumsal Bilgi Yönetimi**
Kurum içi doküman arama, hukuki doküman analizi, tıbbi literatür
taraması gibi alanlarda RAG kullanımı yaygındır. Örneğin, bir sağlık araştırma asistanı RAG modeli,
bir tıbbi veritabanından ilgili makaleleri getirip doktorun sorduğu soruya dayalı derlenmiş bir cevap
verebilir

---

## 2. Temel Kavramlar

### Bilgi Getirme (Retrieval)
Bilgi getirme, bir kullanıcı sorgusuna yanıt olarak büyük bir veri koleksiyonundan ilgili bilgi parçalarını
bulma işlemidir. Başka bir deyişle, doğru bilgiyi arama problemidir. Bu kapsamda bilgi getirme sistemleri,
sorgudaki anahtar kelime ve kavramlara göre dokümanları tarar ve en alakalı sonuçları geri döndürür .
Örneğin bir arama motoru, kullanıcının girdiği sorguya uygun web sayfalarını listelerken bilgi getirme
tekniklerini kullanır. RAG bağlamında, LLM’e entegre edilen bilgi getirme modülü, modelin parametrelerinde
yer almayan harici bilgileri bulup modelin kullanımına sunar.

### Metin Üretme (Generation)
Metin üretimi, bir yapay zeka modelinin verilen girdiye dayanarak yeni ve anlamlı doğal dil metni
oluşturma sürecidir. Bu süreçte model, dil bilgisini ve istatistiksel örüntüleri kullanarak birer birer kelimeler
veya cümleler üretir. Genellikle metin üretimi yapan dil modelleri, bir başlangıç prompt (tetikleyici metin)
alır ve olasılıksal olarak sıradaki kelimeyi tahmin ederek çıktıyı genişletir. Bu döngü, istenen uzunluğa
ulaşana dek veya model bir bitiş belirtecine ulaşana kadar devam eder. Örneğin, “Bir kedi ve köpek…”
şeklinde başlayan bir cümleyi tamamlaması istendiğinde, model eğitim sırasında öğrendiği dil kalıplarına
dayanarak muhtemel devamı yazar. Önemli olan, üretilen metnin dilbilgisel açıdan doğru, tutarlı ve verilen
bağlama uygun olmasıdır. 

### RAG'ın Klasik Modellere Göre Farkları

Retrieval-Augmented Generation, klasik yani yalnızca eğitim verilerine dayalı üretken modellere kıyasla
birkaç önemli avantaja sahiptir:

- Güncel ve dinamik bilgi erişimi
RAG, modelin eğitim verilerinden daha taze olabilecek bilgilere erişim
sağlar. LLM’nin eğitildiği veri zamanla eskiyebilir; oysa RAG modeli, harici bilgi kaynağı sürekli
güncellenebildiği için her zaman güncel veriyi kullanabilir

- Bağlamsal doğruluk ve özelleştirme
Klasik modeller genelleştirilmiş bilgi sunarken, RAG
sistemine entegre edilen bilgi havuzu daha bağlama özgü veriler içerebilir. Bu sayede model, belirli bir
sektör veya kuruluşa ait özel bilgileri dahi yanıtlarına yansıtabilir.Örneğin, kurumsal bir RAG
modeli kendi şirketinizin iç dokümanlarını kullanarak soruları yanıtlayabilir, oysa genel bir LLM bunu
bilemez. Örneğin, kurumsal bir RAG
modeli kendi şirketinizin iç dokümanlarını kullanarak soruları yanıtlayabilir, oysa genel bir LLM bunu
bilemez.

- Azaltılmış halüsinasyon

Dış kaynaklardan getirilen doğrulanabilir veriler, modelin yanlış veya
uydurma bilgiler üretme riskini azaltır. Model, zeminlenmiş (grounded) olduğunda, parametrelerine
“baked-in” hatalı bilgiler yerine güvenilir kaynaklara dayanır. Bu da LLM’nin halüsinasyon ihtimalini
düşürür.
- Kaynak şeffaflığı

RAG çıktılarının dayandığı bilgi parçaları genellikle izlenebilir durumdadır.
Getirilen belgelerin kaynağı bilindiği için modelin cevabının hangi kaynaktan geldiği görülebilir;
dolayısıyla kullanıcı gerektiğinde cevabı doğrulayabilir veya hatalı ise kaynağını güncelleyebilir .
Klasik modellerde ise cevabın kaynağı modelin içinde belirsiz bir şekilde gömülüdür.

- Düşük bakım maliyeti

Yalnız LLM kullanan bir sistemde modelin bilgi tazelemesi için
yeniden eğitme veya ek eğitim (fine-tuning) gerekir ki bu hem zaman hem kaynak açısından
maliyetlidir. RAG yaklaşımında ise bilgi tabanını güncellemek (ör. yeni dokümanlar eklemek) yeterli
olduğundan bakım maliyeti daha düşüktür. Bu yöntem, sık sık model eğitimi yapmaktan daha
hesaplı bir yoldur.

Diğer yandan, RAG modelleri bu ek bileşenleri nedeniyle klasik modellere göre daha karmaşık bir mimariye
sahiptir. Bu karmaşıklık, doğru bir şekilde yönetilmezse performans darboğazları veya entegrasyon
sorunları oluşturabilir.
---

## 3. Teknik Bileşenler

### Transformer Modelleri

RAG sistemlerinin temelinde genellikle Transformer mimarisiyle eğitilmiş dil modelleri bulunur.
Transformer, Google’ın 2017’deki “Attention is All You Need” makalesi ile tanıtılan, dizi verilerindeki ilişkileri
öz-dikkat (self-attention) mekanizmasıyla öğrenen bir sinir ağı türüdür. Bu mimari, uzun metin dizilerinde bile
uzak kelimeler arasındaki bağıntıları verimli bir şekilde yakalayabilir . Örneğin bir Transformer modeli,
bir cümlenin başındaki kelime ile sonundaki kelime arasındaki ilişkiyi tekrar tekrar üzerinden geçmeden
(tekrarlayan ağlar gibi) doğrudan dikkat mekanizması ile öğrenir . BERT, GPT, T5 gibi güncel büyük dil
modelleri Transformer tabanlıdır ve metin anlama ile metin üretme görevlerinde son derece başarılıdır.


RAG mimarisinde Transformer modelleri iki rolde karşımıza çıkar: 

- **Soru/Kullanıcı sorgusu kodlayıcı (encoder):** Girilen soruyu veya prompt’u vektör uzayında temsile dönüştürür. Örneğin bir DPR (Dense
Passage Retriever) modelinde, Transformer bazlı bir kodlayıcı, kullanıcı sorusunu embedding denilen bir
sayısal vektöre çevirir. 
- **Cevap üreten model (decoder/generator):** Bu, genellikle bir seq2seq (dizi-dizi)
Transformer modelidir (BART, T5 gibi) ya da bir GPT türevi olabilir. Retriever’ın getirdiği metin parçalarını ve
orijinal soruyu birlikte girdi olarak alır ve doğal dil çıktı (cevap) üretir. Transformer’ın güçlü dil modelleme
kabiliyeti sayesinde model, gelen ekstra bilgileri bağlama oturtup tutarlı bir yanıt oluşturur.

Özetle, Transformer modelleri RAG’ın hem bellek hem beyin işlevini görür: Bir yandan dil bilgisini öğrenmiş
bir üretici, diğer yandan anlamsal arama yapabilen bir kodlayıcı olarak görev yaparlar.

- **Retriever Encoder**: Sorguyu vektöre çevirir.
- **Generator Decoder**: Getirilen verilerle cevabı üretir.

### Embedding ve Vektör Veri Tabanları

Embedding, metin gibi yapılandırılmamış verileri sayısal vektörler olarak temsil etme yöntemidir. Bir cümle
veya belge, eğitilmiş bir dil modeli yardımıyla çok boyutlu bir uzayda noktaya (vektöre) dönüştürülebilir; bu
vektör, metnin anlamsal içeriğini kodlar. Örneğin “Ankara Türkiye’nin başkentidir” cümlesinin embedding
vektörü, “başkent” ve “Türkiye” gibi kavramları yansıtan bir konumda olacaktır. RAG sistemlerinde
embedding modelleri, soruları ve dokümanları aynı vektör uzayına aktararak anlamsal karşılaştırma
yapılmasını mümkün kılar.

Elde edilen bu vektörleri depolamak ve hızlı arama yapabilmek için vektör veri tabanları kullanılır. Vektör
veri tabanı, her belgenin embedding’ini saklar ve bir arama sorgusunun vektörü ile koleksiyondaki vektörler
arasında benzerlik sorguları yapar. Pinecone, Weaviate, Qdrant gibi özel amaçlı veritabanları bu alanda
yaygındır. Bu veritabanları, milyarlarca vektör arasında milisaniyeler içinde en yakın vektörleri
bulabilecek şekilde optimize edilir. Örneğin, bir RAG uygulamasında şirket dokümanlarının vektörlerini
içeren bir veritabanı olduğunu düşünelim; kullanıcı “yıllık izin politikası nedir?” diye sorduğunda, sorgu
embedding’i hesaplanır ve bu veritabanında en benzer vektörler (yıllık izin politikasının geçtiği
dokümanlardan) hızla getirilir. Bu getirme işlemi çoğunlukla koşul komşu araması (nearest neighbor
search) algoritmalarıyla gerçekleştirilir.


**Özetle:** Embedding’ler, metinleri sayısal olarak karşılaştırılabilir hale getirirken; vektör veri tabanları da bu
karşılaştırmayı büyük ölçekli veri için mümkün kılar. Sonuçta RAG sistemi, soruyla en alakalı bilgi parçalarını
tespit edip getirebilir.

- Metinleri vektör uzayında temsil eder.
- Pinecone, Weaviate, Qdrant gibi vektör veritabanları kullanılır.

### Bilgi Getirme Mekanizmaları
- **Sparse Retrieval**: Bu geleneksel arama yöntemidir. Dokümanlar
içerisinde anahtar kelime eşleşmelerine dayanır; TF-IDF, BM25 gibi algoritmalar metinlerdeki
terimlerin frekansına ve dağılımına bakarak ilgili sonuçları bulur. Anahtar kelime araması, bir sorguda
geçen kelimelerin aynı şekilde dokümanda geçmesine dayanır. Örneğin, “başkent nüfusu Ankara”
şeklinde bir sorgu için sparse arama, içerisinde bu kelimelerin sık geçtiği dokümanları yüksek
skorlarsa, “Ankara” kelimesi geçmeyen ancak aynı anlama gelen bir metni (örneğin “Türkiye’nin
yönetim merkezi”) atlayabilir. **Avantajı**, sonuçların hangi kelimelerden eşleştiği anlaşılabilir
(yorumlanabilir) olması ve genelde daha düşük kaynak gerektirmesidir. Ancak eş anlamlı ifadeleri
veya bağlamsal ilişkileri yakalamakta yetersiz kalabilir.

- **Dense Retrieval**: Bu yaklaşım, yukarıda bahsedilen embedding’leri kullanır
ve anlamsal benzerlik odaklıdır. Sorgu ve dokümanlar vektör uzayında temsil edilir; arama işlemi,
sorgu vektörüne en yakın vektörleri bulmaktır. Bu sayede, tam kelime eşleşmesi olmasa bile benzer
anlamlı içerikler yakalanabilir. Örneğin, “başkent nüfusu Ankara” sorgusu dense aramada,
“Türkiye’nin başkentinin nüfusu…” diye başlayan bir dokümanı yüksek olasılıkla bulacaktır, çünkü
vektör temsilleri anlamsal olarak yakın olacaktır. Dense retrieval genellikle derin öğrenme
modellerinin gücünü kullandığı için daha isabetli anlamsal eşleşmeler sunar, ancak büyük vektör
koleksiyonlarında hızlı arama yapmak için özel altyapı (vektör veritabanı) gerektirir. Günümüzde RAG
sistemlerinde dense retrieval sık tercih edilir, zira LLM’lerin dil bilgisini tamamlayıcı bir şekilde
anlamsal arama yapabilir.

Bir RAG uygulamasında bu iki yöntem bir arada da kullanılabilir: Örneğin önce sparse yöntemle hızlı bir ön
eleme yapılıp, sonra kalan adaylar arasından dense yöntemle en iyiler seçilebilir. Ancak genel olarak, dense
retrieval modern RAG sistemlerinin belkemiğidir, çünkü dil modellerinin anlayabildiği şekilde kavramsal
benzerlikleri yakalar. Özetlemek gerekirse, sparse arama kelimelere, dense arama anlamlara odaklanır.

## 4. RAG Mimarisi

RAG mimarisi, bir getirici (retriever) modülü ile bir üretici (generator) modülü olmak üzere iki ana
bileşeni içerir. Aşağıdaki şema, RAG framework’ünün modüler yapısını ve bir kullanıcı isteğinden yanıt
oluşana dek gerçekleşen veri akışını göstermektedir.

![alt text](image-1.png)

1) Kullanıcı bir istek/prompt girişi yapar.
2) Bu istek, Retrieval Model (Getirici model) tarafından alınıp
kurumun dahili kaynakları gibi harici bilgi kaynaklarında arama yapmak üzere işlenir.
3) Retrieval Model, yapılandırılmış veritabanlarından veya belge koleksiyonlarından ilgili olabilecek kayıtları sorgular ve bulduğu
sonuçları kullanarak kullanıcının orijinal sorgusunu ek bağlamla zenginleştirir (yani sorguya uygun
bağlamsal bilgilerle birleştirir).
4) Ardından bu bağlamla zenginleştirilmiş prompt, Generation Model
(LLM) olarak adlandırılan üretici modele iletilir. LLM, gelen ek bilgiyle desteklenmiş prompt’u işler ve
kullanıcıya yönelik nihai yanıtı oluşturur. Son aşamada model çıktısı kullanıcıya sunulur.


Yukarıdaki döngü, kullanıcının her sorusu için tekrar eder. İyi bir RAG sistemi, tüm bu adımları olabildiğince
hızlı (tercihen birkaçı saniye içinde) yaparak gerçek zamanlı sohbet deneyimi sunabilir . Örneğin, bir
müşteri destek sohbet botunda kullanıcı “Siparişim ne zaman teslim edilir?” diye sorduğunda, retrieval
modülü sipariş veritabanından ilgili kayıtları çekip LLM’e verir; LLM de bu bilgilerle donanmış bir yanıt üretir.


RAG mimarisinde her modül ayrı geliştirilebilir ve optimize edilebilir: Getirici kısım için istenirse farklı arama
algoritmaları denenebilir, üretici kısım için farklı LLM’ler kullanılabilir. Bu modülerlik sayesinde, klasik tekparça
LLM çözümlerine göre RAG sistemleri daha esnek ve ölçeklenebilir hale gelir. Ancak modüller arası
entegrasyonun iyi tasarlanması önemlidir; aksi takdirde getirilen bilginin yanlış kullanımı veya gecikmeler
gibi sorunlar ortaya çıkabilir.

---

## 5. Avantajlar ve Zorluklar

### Avantajlar
- Güncellik

LLM’nin eğitim verilerinde bulunmayan en yeni bilgilere erişebilir. Örneğin, RAG sayesinde
bir model, dün yayınlanmış bir makaledeki bilgiyi bile yanıtına katabilir; bu, eğitimi aylar önce
tamamlanmış klasik bir model için mümkün değildir

- Sürekli güncelleme

Bilgi kaynağı (örn. belge veri tabanı) kolaylıkla güncellenebilir
olduğundan, sistemi baştan eğitmeye gerek kalmadan yeni bilgilere uyum sağlanır. Bu, daha düşük
bakım maliyeti ve daha hızlı adaptasyon demektir

- Bağlam ve özelleştirme

RAG’ın bilgi deposu, belirli bir alan veya kuruma özgü verilerle
doldurulabilir. Böylece model, genel dünya bilgisinin yanında duruma özel detayları da bilebilir. Sonuç
olarak yanıtlar, kullanıcının bulunduğu bağlama çok daha uygun hale gelir.

- İzlenebilirlik ve düzeltilebilirlik

RAG modelleri, yanıtları desteklemek için kullandıkları kaynakları
bildiği için şeffaflık sunar. Bir yanıtın hangi dokümana dayandığı tespit edilebilir; eğer hata varsa ilgili
doküman düzeltilerek modelin gelecekteki çıktıları da düzeltilebilir. Bu, kurumsal uygulamalarda
denetim ve doğrulama açısından büyük avantajdır.

- Azalan halüsinasyon

Model, cevabını harici belgelerle temellendirdiği için
uydurma veya yanlış bilgi verme olasılığı düşer. RAG kullanımı, LLM’nin “kendi hafızasındaki”
tutarsızlıklardansa gerçek kaynaklara dayanmasını sağlar. Bu da cevapların genel doğruluk ve
güvenilirliğini yükseltir.

### Zorluklar
- Teknik karmaşıklık

RAG, standart bir LLM uygulamasından daha karmaşıktır. Bir arama indeksi
oluşturma, vektör veritabanı yönetimi, belge önişleme gibi ek süreçler gerektirir. Geliştirici ekiplerin,
retrieval mekanizmalarını üretken yapay zekâ ile en iyi şekilde entegre etmeyi öğrenmeleri zaman
alabilir. Yeni bir teknoloji olduğu için bu mimarinin inceliklerini kavramak bir öğrenme eğrisi
gerektirir.


- Ek maliyet ve altyapı gereksinimi

Ek bir arama katmanı olduğundan, RAG uygulamak tek başına LLM
çalıştırmaktan daha maliyetli olabilir. Vektör veritabanı barındırma, indeksleme ve arama işlemleri
için ekstra hesaplama kaynakları gerekir. Yine de sık model yeniden eğitimi yapmaktan ucuz olması,
bu maliyeti genellikle tolere edilebilir kılar.

- Veri modelleme ve chunking

Kurum içi bilgi kütüphanesindeki yapılandırılmış (veritabanı kayıtları) ve
yapılandırılmamış (dokümanlar, makaleler) verilerin nasıl temsil edileceği ve indeksleneceği kritik bir
sorundur. Hangi parçaların ne büyüklükte bölüneceği, hangi metadata alanlarının ekleneceği
gibi konular performansı etkiler. Uygun parçalama (chunking) ve indeksleme stratejileri olmadan
getirici isabeti düşebilir.

- Gerçek zamanlı veri entegrasyonu

RAG’ın ideal senaryolarından biri de modelin sürekli yeni gelen
verilerle beslenebilmesidir. Bunu sağlamak için verileri kademeli ve tutarlı biçimde sisteme aktaran
işlem hatları kurulmalıdır. Örneğin, bir destek sistemi her yeni müşteri kaydını veya yazışmasını
anında vektör indeksine eklemelidir ki model en güncel bilgiyi kullansın.

- Hatalı bilgi yönetimi

Dış kaynaktan gelen bilgi yanlışsa veya model yanlış belgeyi aldıysa yanıta da
yansıyacaktır. Bu durumda hatalı içeriği tanıyıp ayıklamak önem kazanır. Sistemlerin, işe yaramayan
veya alakasız belgeleri filtreleyebilmesi (gerekirse “cevap vermemesi”) gerekir . Ayrıca kullanıcı
veya moderatör geri bildirimiyle hatalı verileri indeksinden kaldırma süreçleri uygulanmalıdır.

Tüm bu zorluklara rağmen, RAG alanındaki hızlı gelişmeler bu sorunlara çözümler üretmeye devam ediyor.
İyi tasarlanmış bir RAG sistemi, zorlukları aşıp avantajlarından en yüksek düzeyde yararlanarak, geleneksel
modellere kıyasla çok daha etkili ve güvenilir bir yapay zeka deneyimi sunabilir.

## 6. Uygulamalı Kısım

Bu bölümde, RAG yaklaşımını pratikte basitçe nasıl gerçekleştirebileceğimizi inceleyeceğiz. Python dilinde
Hugging Face kütüphanesini kullanarak temel bir RAG uygulaması yapacak; ardından bunu küçük bir veri
kümesi üzerinde test edip sonuçları değerlendireceğiz.

### Hugging Face ile Basit RAG Modeli Kurulumu

Hugging Face Transformers kütüphanesi, RAG için önceden eğitilmiş modeller ve araçlar sunmaktadır.
Özellikle Facebook AI tarafından eğitilmiş bir RAG modeli, facebook/rag-sequence-nq adıyla mevcuttur.
Bu model, bir DPR tabanlı retriever ve bir BART tabanlı generator içerir ve NaturalQuestions (NQ) veri kümesi
üzerinde açık uçlu soru-cevap için eğitilmiştir. Kendi veri setimizle de bir RAG sistemi kurmak için Hugging
Face’in esnek API’ını kullanabiliriz.

Aşağıda, basit bir RAG modelinin adım adım kurulumu ve kullanımını gösteren örnek bir Python kodu yer
almaktadır:

```python
from transformers import AutoTokenizer, RagRetriever, RagModel

# Tokenizer ve retriever
tokenizer = AutoTokenizer.from_pretrained("facebook/rag-token-base")
retriever = RagRetriever.from_pretrained(
    "facebook/rag-token-base", index_name="exact", use_dummy_dataset=True
)

# Model yükleme
rag_model = RagModel.from_pretrained("facebook/rag-token-base", retriever=retriever)

# Örnek soru
query = "Paris'te kaç kişi yaşıyor?"
inputs = tokenizer(query, return_tensors="pt")
output_ids = rag_model.generate(**inputs)
answer = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print(answer)
```

> Çıktı: `Paris has a population of about 2.1 million people.`


Yukarıdaki kod, use_dummy_dataset=True ile modelin beraberinde gelen örnek veri indeksini
kullanmaktadır. Gerçek bir kullanımda, kendi belge veri kümemizi modelin retriever’ına vermemiz gerekir.
Örneğin, Hugging Face RagRetriever kendi veri setimizi kullanacak şekilde yapılandırılabilir veya
alternatif olarak LangChain gibi yüksek seviye bir kütüphane ile belge yükleme ve indeksleme yapılıp
Hugging Face’in generative modeline bağlanabilir.


**Kendi veri kümemizi entegre etmek:** Diyelim elimizde sorulara kaynaklık edecek Wikipedia makaleleri
veya şirket dökümanları var. Bu durumda her belgeyi uygun parçalara bölüp ( chunk ) OpenAI Embedding
API veya SentenceTransformer gibi bir modelle embedding vektörlerini çıkarırız. Bu vektörleri bir vektör
veritabanına (ör. FAISS, Pinecone) yükleriz. Ardından Hugging Face RagRetriever bu veritabanına
bağlanacak şekilde ayarlanır (örneğin index_name="custom" ve gerekli dosyalar ile). Model, generate
çağrısı sırasında içsel olarak önce retriever’dan en benzer birkaç dokümanı alır, sonra bunları kullanarak
metin üretir. Bu şekilde, kendi bilgi kaynağımıza dayalı cevaplar elde etmiş oluruz.

### Gerçek Veri Kümesiyle Test

Kurulan RAG modelini gerçek bir veri kümesinde test etmek, performansının anlaşılması için kritiktir.
Örneğin, bir Soru-Cevap RAG sistemi geliştirdiğimizi düşünelim ve elimizde doğruluğunu bildiğimiz sorucevap
eşleşmeleri (test seti) olsun. Bu test verisi üzerinde modelimizi iki açıdan değerlendirebiliriz:

1) **Getirilen Bilginin Kalitesi:** Modelin retrieval modülü sorular için gerçekten ilgili dokümanları
bulabiliyor mu? Bunu ölçmek için klasik bilgi getirme metrikleri kullanılır: Hit Rate (isabet oranı), Mean
Reciprocal Rank (MRR), Normalized Discounted Cumulative Gain (NDCG) gibi ölçütler, arama sonuçlarının
ne kadar başarılı olduğunu gösterir . Örneğin, doğru cevabı içeren doküman ilk 5 sonuç içinde mi,
yoksa listede hiç yok mu? MRR değeri 1’e ne kadar yakınsa model ilk sıralarda doğru belgeyi getiriyor
demektir.

2) **Üretilen Cevabın Kalitesi:** Üretici modelin, getirilen bağlamı kullanarak verdiği yanıt ne kadar doğru
ve tutarlı? Exact Match veya F1 skoru gibi metrikler, eğer cevabın tek bir doğru karşılığı varsa
kıyaslama için kullanılabilir (özellikle sınav tarzı sorularda). Ancak açık uçlu sorularda değerlendirme
daha çok niteliksel yapılır: Doğruluk (faithfulness) – cevaptaki bilgiler kaynağa sadık mı? Alaka düzeyi
(relevance) – soru ile gerçekten ilgili mi? Akıcılık ve tutarlılık – cevap iyi bir dilbilgisel bütünlükte mi? Bu
kriterler genellikle insan değerlendirmesiyle veya gelişmiş otomatik metriklerle incelenir .
Özellikle RAG için, modelin cevabının kaynağa ne kadar bağlı kaldığı (faithfulness) çok önemlidir;
çünkü amaç, LLM’nin kafasından uydurmasını önleyip kaynaklara dayanmasını sağlamaktır.


Bir örnek senaryoda, elimizde her sorunun doğru cevabını içeren belgeler listesi olsun. Retrieval
modülümüzün performansını %80 Top-3 isabet oranı (yani soruların %80’inde ilk 3 getirilen dokümandan en
az biri doğru cevabı içeriyor) olarak ölçtüysek ve generation modülü de bu bağlam varken soruların %70’ine
tam doğru yanıt veriyorsa, bu oldukça iyi bir başlangıç demektir. Zayıf noktalarda (örn. bazı sorular için
alakasız belgeler getirilmişse veya model belge içindeki kritik bilgiyi kullanmamışsa) iyileştirmeler yapılır:
Belge indeksine daha fazla bağlamsal bilgi eklenebilir, prompt mühendisliği ile modele verilen bağlam
formatı düzeltilebilir, veya model gerektiğinde “Bu soruya elimdeki bilgiyle yanıt veremem.” diyebilecek
şekilde ayarlanabilir.


Performans değerlendirmesinde unutulmaması gereken nokta, RAG sisteminin iki aşamalı olduğudur –
dolayısıyla her aşamanın ayrı ayrı ve birlikte değerlendirilmesi gerekir. Retrieval aşaması güçlü değilse,
generative model ne kadar iyi olursa olsun doğru cevaba ulaşamayacaktır. Tersi durumda ise yanlış belge
seçilse bile model halâ makul bir cevap üretebilir ama bu yanıltıcı olacaktır. Bu nedenle metrikler ve testler
tasarlanırken hem getirilen içerik hem de üretilen yanıt dikkatlice analiz edilmelidir.

### Performans ölçümleri ve değerlendirme

Yukarıdaki test sürecinde bahsedilen metrikleri özetlemek gerekirse, RAG sistemleri için çift yönlü bir
değerlendirme stratejisi benimsenir:
 
- **Bilgi Getirme Performansı:** Arama sonuçlarının kalitesi, bilgi getirme literatüründen gelen
metriklerle ölçülür. Precision@K, Recall@K (ilk K sonuç içinde doğru belgenin bulunma oranı), MRR
(Mean Reciprocal Rank) – doğru belgenin listede ne kadar üstlerde çıktığını gösterir – veya NDCG –
sıralamanın hem ilgililik hem pozisyon olarak ne kadar optimal olduğunu ölçer – sık kullanılan
metriklerdir . Örneğin, MRR değeri 0.9 üzeri olan bir retrieval modülü, çoğu soruda ilk veya ikinci
sırada isabet sağlıyor demektir.

- **Cevap Üretme Performansı:** Üretilen metnin kalitesi, eğer mümkünse doğru cevaba kelime
kelime benzerlik (F1, BLEU vb.) metrikleriyle; değilse anlamsal ve içerik temelli kriterlerle
değerlendirilir. İçeriğin faithfulness (kaynağa sadakati) ve relevance (soruya uygunluğu) burada kilit rol
oynar . Ayrıca zararsızlık (non-harmfulness) gibi genel dil modeli ölçütleri de göz önünde
bulundurulur – modelin yanlış bilgi vermemesi kadar, saldırgan veya uygunsuz yanıtlar üretmemesi
de önemlidir.

Geliştiriciler, RAG sistemlerini geliştirirken bu metriklerde iyileşme görüp görmediklerine bakarak iteratif
şekilde modeli ve arama modülünü optimize eder. Örneğin, Top-K doğruluk oranı düşükse, embedding
modelini iyileştirmek veya belge indeksine daha fazla içerik eklemek düşünülebilir. Cevaplar bağlama sadık
değilse, prompt’ta kaynak metin alıntıları eklemek veya modelin çıktısında kaynak belirtmesini sağlamak
(citation) gibi yöntemler uygulanabilir.

Sonuç olarak, RAG sistemlerinin performansı hem bilgi getirme hem metin üretme bileşenlerinin
uyumlu çalışmasına bağlıdır. İyi bir değerlendirme ve iyileştirme süreci ile RAG, basit bir LLM’e göre çok
daha doğru, güncel ve güvenilir sonuçlar verebilen bir çözüm sunar.

## 7. Gerçek Hayatta Kullanım

Retrieval-Augmented Generation konsepti, günümüzde birçok büyük teknoloji şirketi ve proje tarafından
benimsenmiş durumdadır. Aşağıda, gerçek dünyada RAG kullanımına dair bazı önemli örnek ve vaka
çalışmalar yer almaktadır:

- **OpenAI ChatGPT Retrieval Plugin**

OpenAI, geliştirdiği ChatGPT modeli için RAG
yaklaşımını destekleyen özellikler sunmuştur. Örneğin, ChatGPT’nin Tarama (Browsing) ve Bilgi
Getirme Eklentisi (Retrieval Plugin), modele harici bilgi kaynaklarından arama yapma imkanı tanır.
Kullanıcı bir soruya yanıt isterken eğer modelin bilgi eklentisi açıksa, model önce ilgili dokümanları
veya web sayfalarını arayıp bulur, sonra bunları kullanarak cevabı hazırlar. Bu tam olarak RAG
mantığıyla çalışır ve ChatGPT’nin kapalı beta plugin ekosisteminde belgeler arasında arama yaparak
soruları yanıtlama gibi kullanım senaryoları gerçekleştirilmiştir. Örneğin OpenAI’nin dokümantasyonunda, bir müşteri destek GPT-4 botunun şirketin bilgi bankasındaki geçmiş destek kayıtlarını arayıp benzer vakalardaki çözümleri yeni soruya uygulaması senaryosu anlatılır – bu
sayede bot, kendi eğitim datasında olmayan şirket özeline ait güncel bilgileri de kullanabilir. Sonuç olarak OpenAI, RAG’ı ChatGPT’nin daha güvenilir ve güncel olması için önemli bir araç
olarak konumlandırmıştır.

- **Meta BlenderBot 3 ve Atlas**

RAG terimi ilk olarak Facebook AI Research
(şimdi Meta AI) ekibinin 2020 yılında yayınladığı bir akademik makalede ortaya atıldı. Meta, RAG
konseptini özellikle bilgi yoğun görevlerde (knowledge-intensive tasks) dil modellerinin
performansını artırmak üzere bir “ince ayar tarifi” olarak tanımlamıştı. Bu araştırmadan beri Meta,
RAG alanında aktif rol oynamaktadır. Örneğin, Meta AI’ın geliştirdiği BlenderBot 3 isimli 175 milyar
parametreli sohbet robotu, internetten arama yapabilme yeteneği ile donatılmıştır – bu da ona,
konuşma sırasında güncel bilgi getirme ve onu cevaba yedirme olanağı verir. BlenderBot 3,
konuştuğu konular hakkında web’de arama yaparak içeriğini güncelleyebildiği için retrievalaugmented
conversation (bilgi ile güçlendirilmiş diyalog) örneği sunmuştur ve bu sayede
halüsinasyon oranını düşürdüğü belirtilmiştir.  Meta ayrıca Atlas adını verdiği, retrievalaugmented
yaklaşımla eğitilmiş bir dil modeli duyurmuş ve bunun az örnekle öğrenme (few-shot
learning) başarısına dikkat çekmiştir.  Özetle, Meta hem araştırma düzeyinde RAG kavramını
literatüre kazandırmış hem de sohbet botları gibi uygulamalarda bu yaklaşımı gerçek dünyaya
taşımıştır. Özetle, Meta hem araştırma düzeyinde RAG kavramını
literatüre kazandırmış hem de sohbet botları gibi uygulamalarda bu yaklaşımı gerçek dünyaya
taşımıştır. 

- **Microsoft Bing Chat & Copilot**

Microsoft’un OpenAI iş birliğiyle geliştirdiği Bing Chat, RAG’ın en
popüler kullanım örneklerinden biridir. Bing Chat, kullanıcı sorgusunu aldıktan sonra web’de arama
yapar, bulduğu sayfalardan ilgili pasajları seçer ve daha sonra GPT-4 tabanlı bir model bu pasajları
okuyarak cevabı üretir. Canlı internete bağlı bu sohbet robotu, kullanıcıya her cevabın dayandığı
kaynak linklerini de sunarak RAG’ın “kanıta dayalı cevap” ilkesini gösterir. Aynı şekilde, Microsoft
365 Copilot sistemi de kullanıcı belgeleri, e-postaları vb. tarayarak LLM’e bağlam sağlamakta, örneğin
bir Word belgesini özetlerken belgenin içeriğini retrieval ile alıp yanıtı oluşturmaktadır. Bu
uygulamalar, arka planda RAG mimarisiyle güçlendirilmiş LLM örnekleridir ve milyonlarca kullanıcı
tarafından günlük olarak kullanılmaktadır.

- **Cohere RAG tabanlı özel danışman botları**

OpenAI ve Meta dışında, Cohere gibi yapay zeka girişimleri de RAG’ı
pratik ürünlerinde kullanıyor. Örneğin Cohere, bir seyahat danışmanına entegre RAG tabanlı sohbet
botu prototipi geliştirmiştir. Bu bot, Kanarya Adaları’ndaki bir tatil kiralamasına dair soruları, şirketin
veritabanından çektiği bağlamsal bilgilerle yanıtlar. Kullanıcının “yakınlarda plaj var mı?” gibi
sorularına, veriye dayalı olarak “500 metre mesafede plaj bulunmaktadır ve cankurtaran hizmeti
vardır” tarzında doğrulanmış bilgiler içeren cevaplar verebilmiştir. Benzer şekilde pek çok
startup ve proje, özel veriyle sohbet (chat with your data) konsepti altında RAG tekniklerini uyguluyor
– örneğin hukuki danışmanlık için hukuk dokümanlarını, finans asistanı için piyasa verilerini veya
tıbbi destek için araştırma makalelerini LLM’lere entegre eden çözümler geliştiriliyor.

- **IBM Watsonx, Oracle AI Solutions**

Büyük teknoloji firmaları da RAG’ı kendi ürünlerine
entegre etmeye başladı. IBM’in 2023’te tanıttığı watsonx platformu, kurumsal müşteriler için RAG
destekli LLM çözümleri sunmaktadır. Oracle ise veritabanı ve bulut altyapısını kullanarak RAG’lı
yapay zeka servisleri geliştirmekte, özellikle şirket içi doküman analizinde RAG’ın verimliliğine dikkat
çekmektedir. Örneğin, Oracle’ın gösterdiği bir senaryoda RAG, çağrı merkezi görüşme kayıtlarını
tarayarak en ilgili çözüm önerilerini çıkaran bir destek aracı olarak kullanılmıştır. 

Gerçek dünya uygulamaları göstermiştir ki, RAG yaklaşımı sayesinde yapay zeka sistemleri hem daha
güncel bilgiye dayalı hem de daha güvenilir hale gelebilmektedir. Özellikle bilgi yoğun alanlarda ve hızlı
güncellenen konularda, RAG tabanlı çözümler klasik LLM yaklaşımlarının yerini almaya başlamıştır.
Önümüzdeki dönemde, arama motorlarından kurumsal asistanlara kadar pek çok alanda RAG’ın standardın
bir parçası haline gelmesi beklenmektedir. Bu da, yapay zeka sistemlerinin insanlara sunduğu faydayı
artırırken, yanlış bilgi riskini azaltacaktır
---

## Kaynaklar
- OpenAI
- Meta AI
- IBM Research
- Oracle
- Weaviate
- Hugging Face
- Pinecone
- NVIDIA
- K2View
- Restack

RAG üzerine literatürde ve sektörde yayımlanmış çeşitli kaynaklar bu dokümanın
hazırlanmasında kullanılmıştır. Belirli alıntılar ilgili bölümlerin sonunda belirtilmiştir. Bunlar arasında IBM,
OpenAI, Oracle gibi güvenilir kurumsal kaynakların yanı sıra, Weaviate, Pinecone gibi teknoloji bloglarından
ve Hugging Face dokümantasyonundan yararlanılmıştır. RAG kavramının temelleri için Meta AI’ın orijinal
makalesi ve sunulan örnek vakalar için şirketlerin resmi açıklamaları incelenmiştir. Bu kaynaklar, RAG
konusunda daha derinlemesine bilgi edinmek isteyenler için yol gösterici olacaktır.

---

Bu doküman Retrieval-Augmented Generation (RAG) konusunda temel ve ileri düzey bilgileri özetlemektedir. Detaylı uygulamalar ve akademik makaleler için yukarıdaki kaynaklar incelenebilir.

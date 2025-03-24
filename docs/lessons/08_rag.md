# Retrieval-Augmented Generation (RAG): Temelden İleri Düzeye Ders Dokümanı

## Giriş

### RAG Nedir?
Retrieval-Augmented Generation (RAG), büyük dil modellerinin (LLM) dış bilgi kaynaklarını kullanarak metin üretmesini sağlayan bir yapay zeka mimarisidir. Kısaca, bir LLM’e entegre edilen bilgi getirme (retrieval) mekanizması sayesinde model, yanıt üretirken eğitim verilerinin ötesindeki güncel ve güvenilir bilgilere erişebilir. Bu teknik ile model çıktıları kanıtlara dayalı hale gelir ve daha isabetli olur. RAG yaklaşımı, doğal dil işleme alanında bilgi çekme (retrieval) ve metin üretimi (generation) yeteneklerini tek bir çatı altında birleştirir; böylece modeller daha derin ve bilgi odaklı cevaplar üretebilir.

### Neden Önemlidir?
Geleneksel büyük dil modelleri eğitim aldıkları veriyle sınırlıdır ve zamanla bilgilerinin güncelliğini yitirir. Bu modeller, parametrelerine “gömülü” olmayan yeni bilgiler karşısında halüsinasyon diyebileceğimiz uydurma cevaplar verebilir. RAG, LLM’lerin güncel ve doğrulanabilir bilgiye erişimini sağlayarak bu sorunları giderir. Temel modeli yeniden eğitmeye gerek kalmadan, modele harici veri kaynaklarından hedeflenmiş bilgiler sunulur; model de bu sayede bağlama uygun, tutarlı ve güncel yanıtlar oluşturabilir. Sonuç olarak RAG, LLM’lerin tek başına yapabildiklerinin ötesine geçip yanıt kalitesini artırır ve hatalı çıkarımları azaltır. Ayrıca, RAG yaklaşımı sayesinde bir modelin bilgi tabanı istenildiği zaman güncellenebildiğinden, modeli yeniden eğitmenin yüksek maliyetinden kaçınılır.

### Kullanım Alanları
RAG mimarisi, geniş bir uygulama yelpazesinde kullanılır. Aşağıda bazı önemli kullanım alanları yer almaktadır:

- **Soru-Cevap ve Arama Motorları:** RAG, arama motorları ve açık uçlu soru-cevap sistemlerinde güncel bilgiye dayalı cevaplar vermek için idealdir. Örneğin, Bing gibi modern arama asistanları, web’den ilgili içerikleri getirip dil modeli ile cevabı derleyerek kullanıcılara sunar.
- **Müşteri Desteği Chatbotları:** Şirketler, ürün ve hizmet bilgilerini içeren bilgi tabanlarını LLM’lere entegre ederek müşteri sorularına doğru yanıtlar verir. OpenAI’nin ChatGPT modelinin knowledge retrieval özelliği ile destek ekibi botlarının, geçmiş destek kayıtlarını sorgulayıp güncel ve şirket-özel cevaplar üretmesi buna örnek verilebilir.
- **Kişisel Asistanlar:** Kişisel dokümanlar, e-postalar veya notlar üzerinde çalışan yapay zeka asistanları RAG’den faydalanır. Örneğin, Notion’ın Ask AI özelliği ya da Microsoft’un Copilot sistemi, kullanıcının kendi verilerinden arama yaparak soruları yanıtlar ve belge özetleme gibi işlemleri gerçekleştirir.
- **İçerik Öneri Sistemleri:** RAG, geleneksel olarak karmaşık model kombinasyonları gerektiren içerik tavsiye problemlerini basitleştirebilir. Bir LLM’in genel bilgisini, kullanıcının özel tercih verileriyle birleştirerek kişiselleştirilmiş öneriler oluşturmak mümkündür.
- **Kurumsal Bilgi Yönetimi:** Kurum içi doküman arama, hukuki doküman analizi, tıbbi literatür taraması gibi alanlarda RAG kullanımı yaygındır. Örneğin, bir sağlık araştırma asistanı RAG modeli, bir tıbbi veritabanından ilgili makaleleri getirip doktorun sorduğu soruya dayalı derlenmiş bir cevap verebilir.

## Temel Kavramlar

### Bilgi Getirme (Retrieval) Nedir?
Bilgi getirme, bir kullanıcı sorgusuna yanıt olarak büyük bir veri koleksiyonundan ilgili bilgi parçalarını bulma işlemidir. Başka bir deyişle, doğru bilgiyi arama problemidir. Bu kapsamda bilgi getirme sistemleri, sorgudaki anahtar kelime ve kavramlara göre dokümanları tarar ve en alakalı sonuçları geri döndürür​. Örneğin bir arama motoru, kullanıcının girdiği sorguya uygun web sayfalarını listelerken bilgi getirme tekniklerini kullanır. RAG bağlamında, LLM’e entegre edilen bilgi getirme modülü, modelin parametrelerinde yer almayan harici bilgileri bulup modelin kullanımına sunar.

### Metin Üretme (Generation) Süreci Nasıl İşler?
Metin üretimi, bir yapay zeka modelinin verilen girdiye dayanarak yeni ve anlamlı doğal dil metni oluşturma sürecidir. Bu süreçte model, dil bilgisini ve istatistiksel örüntüleri kullanarak birer birer kelimeler veya cümleler üretir​. Genellikle metin üretimi yapan dil modelleri, bir başlangıç prompt (tetikleyici metin) alır ve olasılıksal olarak sıradaki kelimeyi tahmin ederek çıktıyı genişletir. Bu döngü, istenen uzunluğa ulaşana dek veya model bir bitiş belirtecine ulaşana kadar devam eder. Örneğin, “Bir kedi ve köpek…” şeklinde başlayan bir cümleyi tamamlaması istendiğinde, model eğitim sırasında öğrendiği dil kalıplarına dayanarak muhtemel devamı yazar. Önemli olan, üretilen metnin dilbilgisel açıdan doğru, tutarlı ve verilen bağlama uygun olmasıdır. Örneğin, kurumsal bir RAG modeli kendi şirketinizin iç dokümanlarını kullanarak soruları yanıtlayabilir, oysa genel bir LLM bunu bilemez.
### RAG’ın Klasik Üretken Modellere Göre Farkları
- **Güncel ve Dinamik Bilgi:** AG, modelin eğitim verilerinden daha taze olabilecek bilgilere erişim sağlar. LLM’nin eğitildiği veri zamanla eskiyebilir; oysa RAG modeli, harici bilgi kaynağı sürekli güncellenebildiği için her zaman güncel veriyi kullanabilir​.
- **Bağlamsal Doğruluk ve Özelleştirme:** Klasik modeller genelleştirilmiş bilgi sunarken, RAG sistemine entegre edilen bilgi havuzu daha bağlama özgü veriler içerebilir. Bu sayede model, belirli bir sektör veya kuruluşa ait özel bilgileri dahi yanıtlarına yansıtabilir​. 
- **Azaltılmış Halüsinasyon:** Dış kaynaklardan getirilen doğrulanabilir veriler, modelin yanlış veya uydurma bilgiler üretme riskini azaltır. Model, zeminlenmiş (grounded) olduğunda, parametrelerine “baked-in” hatalı bilgiler yerine güvenilir kaynaklara dayanır. Bu da LLM’nin halüsinasyon ihtimalini düşürür.
- **Kaynak Şeffaflığı:** RAG çıktılarının dayandığı bilgi parçaları genellikle izlenebilir durumdadır. Getirilen belgelerin kaynağı bilindiği için modelin cevabının hangi kaynaktan geldiği görülebilir; dolayısıyla kullanıcı gerektiğinde cevabı doğrulayabilir veya hatalı ise kaynağını güncelleyebilir​. Klasik modellerde ise cevabın kaynağı modelin içinde belirsiz bir şekilde gömülüdür.
- **Esneklik ve Düşük Bakım Maliyeti:** Yalnız LLM kullanan bir sistemde modelin bilgi tazelemesi için yeniden eğitme veya ek eğitim (fine-tuning) gerekir ki bu hem zaman hem kaynak açısından maliyetlidir. RAG yaklaşımında ise bilgi tabanını güncellemek (ör. yeni dokümanlar eklemek) yeterli olduğundan bakım maliyeti daha düşüktür​. Bu yöntem, sık sık model eğitimi yapmaktan daha hesaplı bir yoldur​. 

Diğer yandan, RAG modelleri bu ek bileşenleri nedeniyle klasik modellere göre daha karmaşık bir mimariye sahiptir. Bu karmaşıklık, doğru bir şekilde yönetilmezse performans darboğazları veya entegrasyon sorunları oluşturabilir (aşağıda Zorluklar bölümünde ele alınacaktır).

## Teknik Bileşenler

### Transformer Modelleri

RAG sistemlerinin temelinde genellikle Transformer mimarisiyle eğitilmiş dil modelleri bulunur. Transformer, Google’ın 2017’deki “Attention is All You Need” makalesi ile tanıtılan, dizi verilerindeki ilişkileri öz-dikkat (self-attention) mekanizmasıyla öğrenen bir sinir ağı türüdür. Bu mimari, uzun metin dizilerinde bile uzak kelimeler arasındaki bağıntıları verimli bir şekilde yakalayabilir​.Örneğin bir Transformer modeli, bir cümlenin başındaki kelime ile sonundaki kelime arasındaki ilişkiyi tekrar tekrar üzerinden geçmeden (tekrarlayan ağlar gibi) doğrudan dikkat mekanizması ile öğrenir​. BERT, GPT, T5 gibi güncel büyük dil modelleri Transformer tabanlıdır ve metin anlama ile metin üretme görevlerinde son derece başarılıdır.

RAG mimarisinde Transformer modelleri iki rolde karşımıza çıkar:

* **Soru/Kullanıcı sorgusu kodlayıcı (encoder):** Girilen soruyu veya prompt’u vektör uzayında temsile dönüştürür. Örneğin bir DPR (Dense Passage Retriever) modelinde, Transformer bazlı bir kodlayıcı, kullanıcı sorusunu embedding denilen bir sayısal vektöre çevirir.
* **Cevap üreten model (decoder/generator):** Bu, genellikle bir seq2seq (dizi-dizi) Transformer modelidir (BART, T5 gibi) ya da bir GPT türevi olabilir. Retriever’ın getirdiği metin parçalarını ve orijinal soruyu birlikte girdi olarak alır ve doğal dil çıktı (cevap) üretir. Transformer’ın güçlü dil modelleme kabiliyeti sayesinde model, gelen ekstra bilgileri bağlama oturtup tutarlı bir yanıt oluşturur.

Özetle, Transformer modelleri RAG’ın hem bellek hem beyin işlevini görür: Bir yandan dil bilgisini öğrenmiş bir üretici, diğer yandan anlamsal arama yapabilen bir kodlayıcı olarak görev yaparlar.

### Embedding’ler ve vektör veri tabanları

**Embedding**, metin gibi yapılandırılmamış verileri sayısal vektörler olarak temsil etme yöntemidir. Bir cümle veya belge, eğitilmiş bir dil modeli yardımıyla çok boyutlu bir uzayda noktaya (vektöre) dönüştürülebilir; bu vektör, metnin anlamsal içeriğini kodlar. Örneğin “Ankara Türkiye’nin başkentidir” cümlesinin embedding vektörü, “başkent” ve “Türkiye” gibi kavramları yansıtan bir konumda olacaktır. RAG sistemlerinde embedding modelleri, soruları ve dokümanları aynı vektör uzayına aktararak anlamsal karşılaştırma yapılmasını mümkün kılar​.

Elde edilen bu vektörleri depolamak ve hızlı arama yapabilmek için vektör veri tabanları kullanılır. Vektör veri tabanı, her belgenin embedding’ini saklar ve bir arama sorgusunun vektörü ile koleksiyondaki vektörler arasında benzerlik sorguları yapar. Pinecone, Weaviate, Qdrant gibi özel amaçlı veritabanları bu alanda yaygındır. Bu veritabanları, milyarlarca vektör arasında milisaniyeler içinde en yakın vektörleri bulabilecek şekilde optimize edilir. Örneğin, bir RAG uygulamasında şirket dokümanlarının vektörlerini içeren bir veritabanı olduğunu düşünelim; kullanıcı “yıllık izin politikası nedir?” diye sorduğunda, sorgu embedding’i hesaplanır ve bu veritabanında en benzer vektörler (yıllık izin politikasının geçtiği dokümanlardan) hızla getirilir. Bu getirme işlemi çoğunlukla koşul **komşu araması (nearest neighbor search)** algoritmalarıyla gerçekleştirilir.


 Embedding’ler, metinleri sayısal olarak karşılaştırılabilir hale getirirken; vektör veri tabanları da bu karşılaştırmayı büyük ölçekli veri için mümkün kılar. Sonuçta RAG sistemi, soruyla en alakalı bilgi parçalarını tespit edip getirebilir.

### Bilgi getirme mekanizmaları

Bilgi getirme, sparse (seyrek) ve dense (yoğun) olmak üzere iki temel yaklaşımla gerçekleştirilebilir:

* **Sparse Retrieval (Anahtar Kelime Tabanlı Arama):**  Bu geleneksel arama yöntemidir. Dokümanlar içerisinde anahtar kelime eşleşmelerine dayanır; TF-IDF, BM25 gibi algoritmalar metinlerdeki terimlerin frekansına ve dağılımına bakarak ilgili sonuçları bulur. Anahtar kelime araması, bir sorguda geçen kelimelerin aynı şekilde dokümanda geçmesine dayanır. Örneğin, “başkent nüfusu Ankara” şeklinde bir sorgu için sparse arama, içerisinde bu kelimelerin sık geçtiği dokümanları yüksek skorlarsa, “Ankara” kelimesi geçmeyen ancak aynı anlama gelen bir metni (örneğin “Türkiye’nin yönetim merkezi”) atlayabilir. Avantajı, sonuçların hangi kelimelerden eşleştiği anlaşılabilir (yorumlanabilir) olması ve genelde daha düşük kaynak gerektirmesidir. Ancak eş anlamlı ifadeleri veya bağlamsal ilişkileri yakalamakta yetersiz kalabilir​.
* **Dense Retrieval (Vektör Tabanlı Arama):** Bu yaklaşım, yukarıda bahsedilen embedding’leri kullanır ve anlamsal benzerlik odaklıdır. Sorgu ve dokümanlar vektör uzayında temsil edilir; arama işlemi, sorgu vektörüne en yakın vektörleri bulmaktır. Bu sayede, tam kelime eşleşmesi olmasa bile benzer anlamlı içerikler yakalanabilir. Örneğin, “başkent nüfusu Ankara” sorgusu dense aramada, “Türkiye’nin başkentinin nüfusu…” diye başlayan bir dokümanı yüksek olasılıkla bulacaktır, çünkü vektör temsilleri anlamsal olarak yakın olacaktır. Dense retrieval genellikle derin öğrenme modellerinin gücünü kullandığı için daha isabetli anlamsal eşleşmeler sunar, ancak büyük vektör koleksiyonlarında hızlı arama yapmak için özel altyapı (vektör veritabanı) gerektirir. Günümüzde RAG sistemlerinde dense retrieval sık tercih edilir, zira LLM’lerin dil bilgisini tamamlayıcı bir şekilde anlamsal arama yapabilir​. 


Bir RAG uygulamasında bu iki yöntem bir arada da kullanılabilir: Örneğin önce sparse yöntemle hızlı bir ön eleme yapılıp, sonra kalan adaylar arasından dense yöntemle en iyiler seçilebilir. Ancak genel olarak, dense retrieval modern RAG sistemlerinin belkemiğidir, çünkü dil modellerinin anlayabildiği şekilde kavramsal benzerlikleri yakalar. Özetlemek gerekirse, sparse arama kelimelere, dense arama anlamlara odaklanır.

### RAG Mimarisi

RAG mimarisi, bir getirici (retriever) modülü ile bir üretici (generator) modülü olmak üzere iki ana bileşeni içerir. Aşağıdaki şema, RAG framework’ünün modüler yapısını ve bir kullanıcı isteğinden yanıt oluşana dek gerçekleşen veri akışını göstermektedir​.

![image](https://github.com/user-attachments/assets/337d8fe9-eabc-420f-9e4e-52d9d1c334bf)

1) Kullanıcı bir istek/prompt girişi yapar.
2) Bu istek, Retrieval Model (Getirici model) tarafından alınıp kurumun dahili kaynakları gibi harici bilgi kaynaklarında arama yapmak üzere işlenir.
3) Retrieval Model, yapılandırılmış veritabanlarından veya belge koleksiyonlarından ilgili olabilecek kayıtları sorgular ve bulduğu sonuçları kullanarak kullanıcının orijinal sorgusunu ek bağlamla zenginleştirir (yani sorguya uygun bağlamsal bilgilerle birleştirir).
4) Ardından bu bağlamla zenginleştirilmiş prompt, Generation Model (LLM) olarak adlandırılan üretici modele iletilir. LLM, gelen ek bilgiyle desteklenmiş prompt’u işler ve kullanıcıya yönelik nihai yanıtı oluşturur​


Yukarıdaki döngü, kullanıcının her sorusu için tekrar eder. İyi bir RAG sistemi, tüm bu adımları olabildiğince hızlı (tercihen birkaçı saniye içinde) yaparak gerçek zamanlı sohbet deneyimi sunabilir​. Örneğin, bir müşteri destek sohbet botunda kullanıcı “Siparişim ne zaman teslim edilir?” diye sorduğunda, retrieval modülü sipariş veritabanından ilgili kayıtları çekip LLM’e verir; LLM de bu bilgilerle donanmış bir yanıt üretir.

RAG mimarisinde her modül ayrı geliştirilebilir ve optimize edilebilir: Getirici kısım için istenirse farklı arama algoritmaları denenebilir, üretici kısım için farklı LLM’ler kullanılabilir. Bu modülerlik sayesinde, klasik tek-parça LLM çözümlerine göre RAG sistemleri daha esnek ve ölçeklenebilir hale gelir. Ancak modüller arası entegrasyonun iyi tasarlanması önemlidir; aksi takdirde getirilen bilginin yanlış kullanımı veya gecikmeler gibi sorunlar ortaya çıkabilir.

## Avantaj ve Zorluklar

RAG, doğru uygulandığında üretken yapay zekâ sistemlerine önemli avantajlar kazandırır:


* **Güncellik**: LLM’nin eğitim verilerinde bulunmayan en yeni bilgilere erişebilir. Örneğin, RAG sayesinde bir model, dün yayınlanmış bir makaledeki bilgiyi bile yanıtına katabilir; bu, eğitimi aylar önce tamamlanmış klasik bir model için mümkün değildir​.
* Sürekli Öğrenme ve Güncelleme: Bilgi kaynağı (örn. belge veri tabanı) kolaylıkla güncellenebilir olduğundan, sistemi baştan eğitmeye gerek kalmadan yeni bilgilere uyum sağlanır. Bu, daha düşük bakım maliyeti ve daha hızlı adaptasyon demektir​.
* Bağlam ve Özelleştirme: RAG’ın bilgi deposu, belirli bir alan veya kuruma özgü verilerle doldurulabilir. Böylece model, genel dünya bilgisinin yanında duruma özel detayları da bilebilir. Sonuç olarak yanıtlar, kullanıcının bulunduğu bağlama çok daha uygun hale gelir​
* İzlenebilirlik ve Düzeltilebilirlik: RAG modelleri, yanıtları desteklemek için kullandıkları kaynakları bildiği için şeffaflık sunar. Bir yanıtın hangi dokümana dayandığı tespit edilebilir; eğer hata varsa ilgili doküman düzeltilerek modelin gelecekteki çıktıları da düzeltilebilir​. Bu, kurumsal uygulamalarda denetim ve doğrulama açısından büyük avantajdır.
* Azalan Halüsinasyon ve Artan Doğruluk: Model, cevabını harici belgelerle temellendirdiği için uydurma veya yanlış bilgi verme olasılığı düşer. RAG kullanımı, LLM’nin “kendi hafızasındaki” tutarsızlıklardansa gerçek kaynaklara dayanmasını sağlar​.




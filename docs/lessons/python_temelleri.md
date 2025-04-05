# Python Giriş Ders Notları

## Python Kurulumu ve Giriş

Python, yorumlamalı (interpreted), nesne yönelimli ve yüksek seviyeli bir programlama dilidir​. Okunabilirliği ön planda tutan basit bir sözdizimine sahip olup, güçlü standart kütüphaneleri sayesinde birçok platformda yaygın olarak kullanılmaktadır.Dinamik olarak tür denetimi (dynamic typing) yapar ve bu da geliştirme sürecini hızlandırır. Günümüzde web geliştirme, veri bilimi, yapay zeka, otomasyon gibi pek çok alanda Python tercih edilmektedir.


## Python'un Kurulumu

Python kurulumu işletim sistemine göre farklılık gösterse de oldukça basittir. Öncelikle sisteminizde Python yüklü olup olmadığını kontrol etmek için terminal/komut isteminde **python --version** veya **python3 --version** komutunu çalıştırabilirsiniz​. ğer Python kurulu değilse, aşağıdaki yöntemlerle kurulum yapabilirsiniz:

* **Windows**: Resmi Python web sitesi (Python.org) üzerinden Windows için sağlanan yükleyiciyi indirip çalıştırabilirsiniz. Kurulum sırasında **"Add Python to PATH"** seçeneğini işaretlemeyi unutmayın. Alternatif olarak Windows 10 ve üzeri için Microsoft Store üzerinden de Python kurulumu yapılabilir​.
* **macOS**: En kolay yöntem, Python.org sitesinden macOS için paketlenmiş .pkg yükleyicisini indirip adımları izlemektir. Bunun yanında, Terminal kullanıyorsanız **Homebrew** paket yöneticisi ile **brew install** python komutunu çalıştırarak da Python 3 kurulumu yapabilirsiniz​.
* **Linux** : Birçok Linux dağıtımı Python'ı ön yüklü getirir. Eğer sisteminizde Python 3 yoksa, dağıtımınızın paket yöneticisi ile kurulumu gerçekleştirebilirsiniz. Örneğin **Debian/Ubuntu** tabanlı sistemlerde **sudo apt-get install python3** komutuyla, **Fedora/CentOS** için **sudo dnf install python3** komutuyla kurulum yapılır​. Ayrıca kaynak koddan derleyerek kurulumu da mümkündür.

Kurulumun ardından, terminal/komut isteminde **python** veya **python3** yazarak Python etkileşimli kabuğunu başlatabilir ve başarılı bir kurulum olup olmadığını test edebilirsiniz. Python'un kendi etkileşimli geliştirme ortamı IDLE da kurulumla birlikte gelir ve hızlı bir şekilde Python kodları denemek için kullanılabilir.

## IDE Önerileri

Python kodlamaya başlarken, kodlarınızı yazıp çalıştırabileceğiniz bir geliştirme ortamı seçmek önemlidir. Basit düzenleyicilerden gelişmiş Entegre Geliştirme Ortamlarına (IDE) kadar birçok seçenek bulunmaktadır. İşte popüler birkaç seçenek:

### PyCharm

PyCharm IDE arayüzüne ait bir ekran görüntüsü: bir Python proje klasörü ve kod editörü görünümü. PyCharm, JetBrains tarafından geliştirilmiş, özellikle Python için özelleşmiş güçlü bir IDE’dir. Kod tamamlama, hata ayıklama (debugging), versiyon kontrol sistemleriyle entegrasyon ve zengin eklenti desteği gibi özellikler sunar. Hem ücretsiz Community (Topluluk) sürümü hem de daha gelişmiş özelliklere sahip Professional sürümü vardır. Yeni başlayanlar için kurulumu ve kullanımı nispeten kolay olup, özellikle büyük projelerde kodun düzenlenmesini ve yönetimini kolaylaştırır.

### Visual Studio Code

Visual Studio Code (VS Code), Microsoft tarafından sunulan hafif fakat oldukça güçlü bir kaynak kod editörüdür. Python desteği, Python eklentisi kurularak sağlanır ve bu eklenti sayesinde kod renklendirme, otomatik tamamlama, hata ayıklama ve hatta Jupyter Notebook entegrasyonu mümkün olur. VS Code, bir IDE kadar kapsamlı olmasa da eklenti tabanlı yapısı ile Python geliştirme için sıkça tercih edilir. Ücretsiz ve açık kaynak olması, çapraz platform (Windows, macOS, Linux) desteği ve entegre terminali ile hem yeni başlayanlar hem de profesyoneller için uygun bir ortam sunar.

### Jupyter Notebook

Jupyter Notebook, web tarayıcısı üzerinden çalışan etkileşimli bir geliştirme ortamıdır. Kod, metin, görsel ve matematiksel formülleri bir arada “not defteri” mantığıyla barındırabilir. Özellikle veri bilimi ve yapay zeka alanlarında, adım adım veri analizi yapmak ve sonuçları görselleştirerek sunmak için yaygın olarak kullanılır. Her bir notebook hücresinde Python kodu çalıştırabilir, çıktılarını hemen altında görebilirsiniz. Jupyter Notebook, **Anaconda** dağıtımı içinde hazır gelir veya pip install notebook ile kurulabilir. Ayrıca Jupyter’in gelişmiş bir sürümü olan **JupyterLab**, birden fazla dosya ve konsolu tek arayüzde toplayarak daha entegre bir deneyim sunar.

## Temel Veri Yapıları (list, tuple, dictionary, set)

Python, çeşitli yerleşik veri yapıları (built-in data structures) sunar. En sık kullanılan temel veri yapıları listeler, demetler, sözlükler ve kümelerdir. Bunlar verileri program içerisinde saklamak ve organize etmek için kullanılır:

* **Liste (list):** Köşeli parantez [...] ile gösterilir. Sıralı (ordered) bir veri yapısıdır ve değiştirilebilir (mutable) özelliktedir, yani oluşturulduktan sonra eleman ekleme, silme veya değiştirme işlemleri yapılabilir. ,

**Örnek**:** meyveler = ["elma", "armut", "muz"]** bir liste örneğidir; meyveler[0] ifadesi "elma" değerini verir.

* **Demet (tuple)**: Normal parantez (...) ile gösterilir. Listeye benzer şekilde sıralı bir yapıdır ancak değiştirilemez (immutable). Yani bir kez oluşturulduktan sonra elemanları değiştirilemez. Genellikle sabit bir koleksiyon gerektiğinde veya değiştirilmeyeceğinden emin olunan veriler için kullanılır. Örnek: renkler = ("kırmızı", "yeşil", "mavi"). Bu demetin elemanları sonradan değiştirilemez.
* **Sözlük (dictionary):** Süslü parantez {...} ile tanımlanır ve anahtar-değer (key-value) çiftlerini depolar. Sözlükler sıralı yapıda değildir (Python 3.7+ sürümlerinde ekleme sırasını korusalar da kavramsal olarak sırasız kabul edilir) ve değiştirilebilir (mutable). Her anahtar eşsizdir ve bir değere karşılık gelir.

**Örnek**: **ogrenci = {"ad": "Ahmet", "yas": 20}** bir sözlük olup "ad" ve "yas" anahtarları aracılığıyla ilgili değerlere erişilebilir (ogrenci["ad"] sonucu "Ahmet" verir).
* **Küme (set)**: Süslü parantez veya set() fonksiyonu ile oluşturulur ve benzersiz elemanlardan (tekrar etmeyen) oluşur. Sırasız (unordered) bir yapıdır ve elemanları değiştirilebilir (kendisine yeni eleman eklenip çıkarılabilir ancak sırasız olduğu için indeks ile erişim yapılamaz). Kümeler, matematiksel küme işlemlerini (kesişim, birleşim gibi) destekler.

**Örnek:** **A = {1, 2, 3}** bir küme, **B = {3, 4, 5}** diğer bir küme ise **A & B** kesişim işlemi **{3}** sonucunu verir.

Yukarıdaki veri yapılarından **listeler ve sözlükler değiştirilebilirken, demetler değiştirilemez** yapıya sahiptir. Listeler ve demetler sıralıdır (elemanların indeksi vardır), sözlükler ve kümeler ise sırasız yapılardır (elemanların konumu sabit değildir, bu nedenle indeks kullanılmaz). Programlama sırasında doğru veri yapısını seçmek, verileri verimli ve anlamlı şekilde organize etmek açısından önemlidir.

## Değişkenler ve Veri Tipleri


Python'da değişken tanımlamak için özel bir sözdizimi yoktur; değişkene değer ataması yapıldığında değişken otomatik olarak oluşur. Örneğin **x = 5** yazarak bir değişken tanımlayabiliriz. Değişken isimleri harf, rakam ve altçizgi **_** karakteri içerebilir, ancak rakamla başlayamaz. Python büyük/küçük harf duyarlıdır, yani **sayi** ve **Sayi** farklı değişkenlerdir. Python dinamik tür bağlamalı bir dil olduğu için, bir değişkene atanan değerin tipine göre davranır ve bu tip sonradan değişkenin alacağı yeni değerlere göre değişebilir. Temel veri tiplerinden bazıları şunlardır:

* **Tam sayı (int):** Tamsayı değerleri tutar. Örneğin **a = 42** ile a değişkeni bir tam sayı olur.
* **Ondalıklı sayı (float):** Ondalıklı (kayan noktalı) değerleri tutar. Örneğin **b = 3.14**
* **Metin (str):** Çift veya tek tırnak içerisinde yazılan metin değerleridir. Örneğin **c = "Merhaba"** veya **d = 'Merhaba'**. Python’da karakter (char) tipi yoktur, tek karakter de aslında bir metin (string) olarak temsil edilir.
* **Mantıksal (bool):** İki değerden birini alabilen (True veya False) mantıksal veri tipidir. Koşul ifadelerinde sıkça kullanılır. Örneğin **durum = True.**

Ayrıca Python’da daha karmaşık tipler de vardır (complex, NoneType gibi), ancak başlangıç için yukarıdakiler en yaygın olanlarıdır. Değişkenin tipini öğrenmek için yerleşik type() fonksiyonu kullanılabilir. Örneğin:

```python

x = 10
y = 2.5
z = "Python"
print(type(x), type(y), type(z))
# <class 'int'> <class 'float'> <class 'str'>

```

Yukarıdaki kodda **x** bir int, **y** float, **z** ise str (string) tipindedir. Python’da değişken tipini önceden belirtmeye gerek olmadığı, değer atanmasıyla belirlendiği için, esnek ve hızlı bir şekilde değişken tanımlayabilirsiniz. Ancak bu esneklik, tip uyumsuzluklarından kaynaklanan hatalara da sebep olabileceği için, özellikle büyük projelerde değişkenlerin içerdiği değerlere dikkat etmek gerekir.



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

## Koşullu İfadeler (if, elif, else)

Python'da koşullu ifadeler, belirli bir koşula göre kod parçacıklarının çalıştırılmasını sağlar. En temel haliyle **if** anahtar kelimesiyle başlar, koşul sağlanmazsa **elif** (else if’in kısaltması) ve en sonunda hiçbiri sağlanmazsa else bloğu çalışır. Python’da bloklar, süslü parantezler yerine **girinti (indentation)** ile belirlenir. Örneğin:

``` python
x = 5
if x > 0:
    print("x pozitif bir sayıdır.")
elif x < 0:
    print("x negatif bir sayıdır.")
else:
    print("x sıfıra eşittir.")

```

Yukarıdaki kod, **x** değişkeninin değerine göre üç farklı durumdan birini ekrana yazdıracaktır. Burada **x >** 0 koşulu doğruysa ilk blok çalışır; eğer değilse ve **x < 0** koşulu doğruysa ikinci blok çalışır; her iki koşul da sağlanmazsa else bloğundaki kod devreye girer. elif isteğe bağlıdır ve birden fazla da olabilir. Koşullu ifadelerde karşılaştırma operatörleri **>, <, >=, <=, == (eşit mi) ve != (eşit değil mi)** sıkça kullanılır. Ayrıca koşulları birleştirmek için **and**, **or** ve **not** gibi mantıksal operatörler de kullanılabilir.

## Döngüler (for, while)

Döngüler, belirli bir işlemi birden fazla kez gerçekleştirmek istediğimizde kullanılır. Python'da başlıca iki döngü yapısı vardır: **for** döngüsü ve **while** döngüsü.

* **for döngüsü**: Belirtilen bir koleksiyon (list, tuple, string, vb.) veya bir aralık (range) üzerinde yineleme yapar. Örneğin, 0'dan 4'e kadar sayıları yazdıralım:

``` python
for i in range(5):
    print(i)
```

Bu kod **range(5)** ile **0,1,2,3,4** değerlerini üretecek ve i değişkeni bu değerleri sırayla alarak döngü her döndüğünde **print(i)** çalışacaktır. Sonuç olarak ekrana 0 ile 4 arasındaki sayılar basılır. **for** döngüsü, listeler gibi yineleyebileceğimiz (iterable) veri yapıları üzerinde de kullanılabilir:

``` python
sehirler = ["Ankara", "İstanbul", "İzmir"]
for sehir in sehirler:
    print(sehir)
```
* **while döngüsü:** Belirtilen bir koşul True (doğru) olduğu sürece kod bloğunu tekrarlar. Yani döngüye girmeden önce ve her tekrarın başında koşul kontrol edilir, koşul False olduğunda döngü sona erer. Örneğin 0'dan 4'e kadar sayıları while ile yazdıralım:

``` python
sayi = 0
while sayi < 5:
    print(sayi)
    sayi += 1
```
Bu kod parçasında, sayi 5'ten küçük olduğu sürece döngü devam eder. Her döngü turunda sayi değişkeni 1 arttırılır **(sayi += 1)**, böylece en sonunda koşul False olur ve döngü sonlanır. Dikkat: while döngülerinde koşulun bir noktada False olmasını sağlamazsak sonsuz döngü oluşabilir. Gerekirse döngü içinde **break** ifadesi kullanılarak bir koşul gerçekleştiğinde döngü kırılabilir veya **continue** ile o tur atlanıp döngü başına dönülebilir (bu yapılar ileri düzeyde ele alınabilir).

## Fonksiyon Tanımlama ve Çağırma

Fonksiyonlar, belirli bir görevi yerine getiren ve gerektiğinde çağrılabilen kod bloklarıdır. Python'da fonksiyon tanımlamak için def anahtar kelimesi kullanılır, ardından fonksiyon adı ve parantez içinde parametreler belirtilir. Fonksiyon gövdesi girintili olarak alt satıra yazılır. İsteğe bağlı olarak **return** ifadesi ile bir değer döndürülebilir. Örneğin, basitçe bir karşılama mesajı yazdıran fonksiyon tanımlayalım:

``` python
def selamla(isim):
    print("Merhaba, " + isim + "!")

# Fonksiyonu çağırma
selamla("Ayşe")
```
Bu örnekte **selamla** adında bir fonksiyon tanımladık. **isim** adında bir parametre alıyor ve bu parametreyi kullanarak bir mesaj yazdırıyor. Fonksiyonu çağırırken parantez içinde gerekli argümanı **("Ayşe")** geçtik ve fonksiyon bu değeri alarak çıktı üretti: **Merhaba, Ayşe!**. Bir fonksiyon hesaplama yapıp sonuç döndürebilir:

``` python
def kare(x):
    return x * x

sonuc = kare(5)
print(sonuc)  # 25
```
**kare** fonksiyonu verdiğimiz sayının karesini hesaplayıp **return** ile döndürür. return döngü veya koşul içinde çalıştığında da fonksiyondan çıkar. Fonksiyonlar, kod tekrarını önler ve programı daha modüler hale getirir. Parametre olarak varsayılan değerler verilebilir **(def f(y=0): ...)**, değişken sayıda argüman alabilir (***args**, ****kwargs** gibi ileri konular) ancak bunlar giriş niteliğindeki ders notlarında genellikle daha sonra ele alınır.

## Temel Örnek Uygulamalar

Şimdiye kadar öğrenilenleri pekiştirmek için birkaç basit örnek uygulama yapalım. Bu uygulamalar, koşullu ifadeler, döngüler ve fonksiyon kullanımını göstererek Python'un temel yapılarıyla neler yapılabileceğini ortaya koyacak.

Kullanıcıdan bir sayı alıp pozitif, negatif veya sıfır olduğunu belirten bir program yazalım:


``` python
sayi = int(input("Bir sayı girin: "))
if sayi > 0:
    print("Pozitif")
elif sayi < 0:
    print("Negatif")
else:
    print("Sıfır")
```

Bu program input fonksiyonu ile kullanıcıdan giriş alır, **int(...)** ile bu girişi tamsayıya çevirir ve ardından **if-elif-else** yapısıyla sayının durumunu kontrol ederek sonucu ekrana basar. Örneğin kullanıcı 7 girdiğinde çıktı Pozitif olacaktır; -3 girerse Negatif, 0 girerse Sıfır yazacaktır.

Bir sayının faktöriyelini hesaplayan fonksiyon yazalım. Faktöriyel, 1'den o sayıya kadar olan pozitif tamsayıların çarpımıdır. Örneğin **5! (5 faktöriyel) = 5×4×3×2×1 = 120.**

``` python
def faktoriyel(n):
    sonuc = 1
    for i in range(1, n+1):
        sonuc *= i
    return sonuc

# Fonksiyonu test edelim
print(faktoriyel(5))   # 120
print(faktoriyel(1))   # 1
print(faktoriyel(0))   # 1 (matematiksel olarak 0! = 1 kabul edilir)
```

Burada **faktoriyel** adında bir fonksiyon tanımladık. **n** parametresi alıyor ve **for** döngüsü ile **1**'den **n**'e kadar tüm sayıları **sonuc** üzerinde çarparak biriktiriyor. Sonuç değeri **return** ile döndürülüyor. Örneğin **faktoriyel(5)** çağrısı 120 değerini döndürüyor. Bu fonksiyon içinde **döngü** ve **aritmetik işlem** bir arada kullanılarak küçük bir hesaplama gerçekleştirilmiş oldu. Döngüler ve koşullu ifadeler kullanarak benzer şekilde Fibonacci dizisi hesaplama, asal sayı bulma gibi klasik programlama örnekleri de yapılabilir.

## Modüller ve Kütüphaneler

Burada faktoriyel adında bir fonksiyon tanımladık. n parametresi alıyor ve for döngüsü ile 1'den n'e kadar tüm sayıları sonuc üzerinde çarparak biriktiriyor. Sonuç değeri return ile döndürülüyor. Örneğin faktoriyel(5) çağrısı 120 değerini döndürüyor. Bu fonksiyon içinde döngü ve aritmetik işlem bir arada kullanılarak küçük bir hesaplama gerçekleştirilmiş oldu. Döngüler ve koşullu ifadeler kullanarak benzer şekilde Fibonacci dizisi hesaplama, asal sayı bulma gibi klasik programlama örnekleri de yapılabilir.

### Python’da Modül ve Paket Yapısı

Bir modül, Python kodlarını içeren bir dosyadır (genellikle bir .py dosyası)​.  Kendi yazdığımız veya başkaları tarafından yazılmış modülleri programımıza dahil ederek, içindeki fonksiyon ve değişkenleri kullanabiliriz. Bir modül, örneğin **math.py** isminde bir dosya ise, Python içinde **import math** diyerek bu modülü içe aktarabilir ve math.sqrt(16) gibi modülün tanımladığı fonksiyonları kullanabiliriz. Python’ın standart kütüphanesinde **math**, **datetime**, **random**, **os** gibi birçok hazır modül bulunmaktadır.

Bir **paket** ise bir arada gruplandırılmış modüller kümesidir. Teknik olarak, bir dizin (klasör) içerisindeki birden fazla Python modülünün bir araya gelmesiyle oluşur. Paketler, modülleri mantıksal bir şekilde organize etmeye yarar. Örneğin bir proje içinde **veri_islemleri** adında bir paket, bu paket içinde **oku.py, yaz.py** ve **analiz.py** gibi modüller olabilir. Bu yapıyı Python'a paket olarak tanıtmak için, ilgili klasöre genellikle boş bir __init__.py dosyası konulur (Python 3.3'ten itibaren bu dosya olmadan da paket olarak davranabilen "namespace package" kavramı eklenmiştir). Kısaca, paketler modüllerin koleksiyonudur ve nokta . notasyonu ile alt modüllere erişimi mümkün kılar​.

 Örneğin, **import veri_islemleri.oku** diyerek veri_islemleri paketindeki oku modülünü içe aktarabilirsiniz.

Modül import etmenin çeşitli yolları vardır:

* **import <modül_adı>:** Modülü içe aktarır. Modül içindeki ögelere modül_adı.oge şeklinde erişilir. Örnek: import math ardından math.pi veya math.factorial(5) kullanılabilir.
* **from <modül_adı> import <öge_adı>:** Modülün içindeki belirli bir ögeyi doğrudan alır. Örnek: from math import pi, sqrt ardından doğrudan pi veya sqrt(16) kullanabiliriz.
* **import <modül_adı> as <takma_ad>:** Modülü kısaltma bir ad ile import eder. Örnek: import numpy as np (NumPy kütüphanesi genelde np takma adıyla kullanılır).

Bu yapılar birleştirilebilir (örn. from paket.modul import oge). İyi bir kod organizasyonu için, her dosyanın başında kullanılacak modüller import edilir. Python, modül ararken öncelikle o anki çalışma dizininde, sonra Python yolunda (PATH) belirtilen dizinlerde ve en son standart kütüphane dizinlerinde arama yapar.

### pip ile Paket Yönetimi

Pek çok ek Python kütüphanesi PyPI (Python Package Index) aracılığıyla dağıtılır. pip, Python’un paket yöneticisidir ve bu kütüphanelerin kolayca kurulup yönetilmesini sağlar. Python 3 ile birlikte genellikle pip de otomatik olarak gelmektedir (ayrıca ayrı bir kuruluma gerek kalmaz). pip nedir? En öz tanımıyla "pip, Python için paket yükleyicisidir; Python Package Index’ten (PyPI) ve diğer dizinlerden paketleri kurmak için kullanılır."​

Komut satırından pip kullanımı şu şekildedir:

* Bir paketi kurmak için: pip install paket_adı. Örneğin, pip install requests komutu, HTTP istekleri yapmaya yarayan Requests kütüphanesini sisteminize indirip kuracaktır.
* Bir paketi belirli bir sürüme güncellemek için: **pip install --upgrade paket_adı**
* Kurulu paketleri listelemek için: **pip list**
* Bir paketi kaldırmak (uninstall) için: **pip uninstall paket_adı**

**Not**: Bazı sistemlerde Python 2 ve Python 3 yan yana kuruluysa, pip3 komutunu kullanmanız gerekebilir. Ayrıca, izin problemleri yaşamamak için Linux/MacOS'ta komutun başına sudo eklemek (ya da daha iyisi, sanal ortamlar kullanarak paket kurmak) gerekebilir.

**pip** ile kurulan paketler, Python’ın standart kütüphanesinde olmayan üçüncü parti kütüphanelerdir. Örneğin, veri bilimi için popüler olan **NumPy**, **pandas** gibi kütüphaneleri **pip install numpy pandas** komutuyla yükleyebilir ve programlarınızda kullanmaya başlayabilirsiniz.

## Popüler Yapay Zeka ve Veri Bilimi Kütüphaneleri

Python ekosistemi, yapay zeka ve veri bilimi alanında çok zengin kütüphanelere sahiptir. İşte en popülerlerinden bazıları:

* **NumPy**: Bilimsel hesaplama için temel bir kütüphane olan NumPy, Python diline büyük, çok boyutlu diziler (array) ve matrislerle çalışma desteği ekler ve bu diziler üzerinde yüksek seviyeli matematiksel işlemler yapmayı sağlar​. NumPy, sayısal hesaplamaların çoğunu C dilinde gerçekleştirdiği için Python ile yazılan kodların çok daha hızlı çalışmasını mümkün kılar. Lineer cebir, rastgele sayılar üretme, Fourier dönüşümleri gibi birçok işleve sahiptir.
* **pandas**: pandas, veri manipülasyonu ve analizi için geliştirilmiş açık kaynaklı bir Python kütüphanesidir. Veri yapıları ve veriler üzerinde yapılacak işlemler için kolaylıklar sunar​. Özellikle tabular (tablo benzeri) verileri temsil eden DataFrame yapısı oldukça güçlüdür. CSV, Excel, SQL gibi farklı formatlardaki verileri kolayca okuma/yazma, veriler üzerinde filtreleme, gruplama, birleştirme gibi işlemleri yapma imkanı sağlar. Zaman serisi verileriyle çalışmak için de destek sunar.
* **scikit-learn**: Makine öğrenmesi alanında en popüler kütüphanelerden biridir. scikit-learn, Python için geliştirilmiş ücretsiz ve açık kaynaklı bir makine öğrenmesi kütüphanesidir; çeşitli sınıflandırma, regresyon ve kümeleme algoritmalarını içerir​. Destek vektör makineleri, karar ağaçları, rastgele ormanlar, lojistik regresyon, k-Means gibi pek çok algoritmayı kolay bir arayüzle sunar. Ayrıca veri önişleme, özellik seçimi ve model değerlendirme araçları da barındırır. scikit-learn genellikle NumPy, pandas ve Matplotlib ile birlikte kullanılarak eğitim veri setleri üzerinde model oluşturup tahminler yapmak için kullanılır.
* **TensorFlow**: Google tarafından geliştirilmiş olan TensorFlow, makine öğrenmesi ve özellikle derin öğrenme uygulamaları için kullanılan açık kaynaklı bir yazılım kütüphanesidir. ​TensorFlow, yapay sinir ağlarının eğitiminde ve çalıştırılmasında (inference) yaygın olarak kullanılır. Dağıtık sistemlerde ve GPU'larda yüksek performanslı şekilde çalışabilir. Düşük seviyede hesaplama grafikleri (computation graph) üzerinde çalışırken, aynı zamanda Keras API’si gibi yüksek seviye arabirimlerle kolay model geliştirmeyi de destekler. Görüntü işleme, doğal dil işleme gibi AI görevlerinde sıkça tercih edilen bir platformdur.
* **PyTorch**: Facebook (Meta) tarafından geliştirilmiş açık kaynaklı bir derin öğrenme kütüphanesidir. PyTorch, özellikle araştırma camiasında esnekliği ve kullanım kolaylığı ile öne çıkar ve dinamik hesaplama grafikleri sayesinde model geliştirme ve hata ayıklamayı kolaylaştırır. Temelde Lua dilindeki Torch kütüphanesine dayanır. Bilgisayarlı görü (Computer Vision) ve doğal dil işleme projelerinde yoğun şekilde kullanılmaktadır. PyTorch, derin öğrenme modelleri geliştirmede hızlı prototipleme ile üretim ortamına geçiş arasında köprü kurmayı hedefler. 2016 yılında piyasaya sürülmüş ve o zamandan beri popülaritesi sürekli artmıştır. Günümüzde TensorFlow ile birlikte en çok kullanılan derin öğrenme framework’lerinden biridir.

Yukarıdaki kütüphanelerin her biri, kendi alanlarında adeta birer standart haline gelmiştir. Örneğin, NumPy ve pandas olmadan etkili bir veri analizi yapmak neredeyse mümkün değildir; benzer şekilde TensorFlow ve PyTorch, derin öğrenme modellerini oluşturmak için devasa ekosistemler sunar. Bu kütüphanelerin bir kısmı doğrudan pip ile kurulabilirken (örneğin pip install numpy pandas scikit-learn), TensorFlow ve PyTorch gibi bazıları için platforma özel kuruluma dikkat etmek (örneğin GPU desteği isteme durumu) gerekebilir.

### NumPy Örneği

NumPy ile bir dizi (array) tanımlayalım ve matematiksel bir işlem yapalım:

``` python
import numpy as np

# NumPy array oluşturma
a = np.array([1, 2, 3, 4])
print(a * 2)  # [2 4 6 8]

```

Bu kodda önce **NumPy** kütüphanesini **np** adıyla içe aktardık. **np.array** fonksiyonuyla Python listesine benzer şekilde bir NumPy dizisi oluşturduk. NumPy dizileri üzerinde yapılan **a * 2** gibi işlemler, dizinin her bir elemanına uygulanır (bu özelliğe broadcasting denir). Sonuç olarak **[2 4 6 8]** çıktısını elde ederiz. Bu, Python listelerine göre çok daha hızlı ve kolay bir şekilde vektörel operasyonlar yapmamızı sağlar.

### pandas Örneği

pandas ile bir DataFrame oluşturalım ve bazı basit işlemler yapalım:

``` python
import pandas as pd

# Sözlük kullanarak bir DataFrame oluşturma
veri = {"Ad": ["Ali", "Ayşe", "Mehmet"], "Yaş": [25, 30, 22]}
df = pd.DataFrame(veri)
print(df)
```

Yukarıdaki kodda önce **pandas** kütüphanesini pd takma adıyla import ettik. Sonra veri adında bir sözlük oluşturduk; bu sözlük iki anahtar içeriyor: **"Ad"** ve **"Yaş"**, ve her birinin değerleri listeler. **pd.DataFrame(veri)** ile bu sözlüğü kullanarak bir DataFrame oluşturduk. Ekrana yazdırdığımızda tablo benzeri bir çıktı göreceğiz:

``` python
      Ad  Yaş
0    Ali   25
1   Ayşe   30
2 Mehmet   22
```
Her bir satır otomatik olarak 0,1,2 şeklinde indekslenmiştir. Bu DataFrame üzerinde örneğin df["Ad"] ile sadece Ad sütununu alabilir, df.describe() ile sayısal kolonlar için özet istatistikler elde edebilir, df.sort_values("Yaş") ile Yaş değerine göre sıralama yapabilirsiniz. pandas ile veri okuma/yazma işlemleri de kolaydır (örn. pd.read_csv("dosya.csv") ile CSV okuma gibi).

### scikit-learn Örneği

scikit-learn ile basit bir makine öğrenimi modeli oluşturalım. Örneğin, basit bir lineer regresyon modeli kullanarak örnek bir veri setine uyduralım:


``` python
from sklearn.linear_model import LinearRegression

# Eğitim verisi (X: girişler, y: çıkışlar)
X = [[1], [2], [3]]
y = [2, 4, 6]
model = LinearRegression()
model.fit(X, y)             # Modeli veriye uydur (eğitim)
tahmin = model.predict([[4]])
print(tahmin)  # [8.]

```

Bu kodda LinearRegression modelini içe aktardık. Çok basit bir veri seti tanımladık: **X** giriş olarak **1,2,3** değerleri, y ise karşılık gelen **2,4,6** çıktı değerleri (görüldüğü gibi burada aslında y = 2 * x ilişkisi var). model.fit(X, y) ile modelimizi bu veriye eğittik. Ardından model.predict([[4]]) ile x=4 için tahmin yapmasını istedik. Sonuç [8.] olarak çıktı, yani model 4 girdisi için yaklaşık 8 sonucunu verdi. Bu beklenen bir sonuçtu, çünkü veri doğrusal bir ilişki içeriyordu. Bu örnek, scikit-learn ile bir modeli nasıl oluşturup kullanabileceğimizi çok basit bir şekilde gösteriyor. scikit-learn içinde benzer şekilde sınıflandırma için örneğin LogisticRegression, karar ağaçları için DecisionTreeClassifier gibi birçok algoritma benzer arayüzle kullanılabilir.

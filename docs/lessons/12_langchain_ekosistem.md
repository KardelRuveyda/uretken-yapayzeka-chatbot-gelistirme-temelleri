## LangChain
​LangChain, büyük dil modelleri (LLM'ler) üzerine inşa edilen uygulamaların geliştirilmesini kolaylaştıran açık kaynaklı bir çerçevedir. Bu çerçeve, geliştiricilerin farklı bileşenleri bir araya getirerek karmaşık iş akışları oluşturmasına olanak tanır. Bu iş akışlarına "**chain**" (zincir) adı verilir ve her zincir, belirli bir görevi yerine getirmek için bir dizi adımı sıralı olarak uygular.

![image](https://github.com/user-attachments/assets/c065fe5f-281c-48c4-bf05-22127ceed909)

## LangChain Amaçları

* LLM'lerle etkileşimi kolaylaştırmak
* Zincir (Chain) yapısıyla birden fazla adımı birleştirerek akıllı uygulamalar geliştirmek
* Harici veri kaynakları (veritabanı, API, PDF vb.) ile çalışmak
* İzlenebilir, test edilebilir uygulamalar sunmak

## LangChain Temel Bileşenleri

* **PromptTemplate**: LLM'e sorulacak sorunun şablonunu belirler.
* **LLM**: ChatOpenAI veya benzeri model ile entegre çalışır.
* **OutputParser**: Model çıktısını uygun formata dönüştürür.
* b: Sohbet uygulamalarında bağlam saklar.
* **Chains**: Tüm bu bileşenleri bir zincir yapısında birleştirir.
* **Tools & Agents**: Web tarayıcı, hesap makinesi gibi dış sistemlerle çalışan ajanlar

## LangChain Yan Platformları

* **LangGraph**: Karmaşık iş akışların döngüel grafikler olarak modellenmesini sağlar.
* **LangSmith**: Uygulamaların test edilmesi, hata ayıklanması ve gözlemlenmesini sağlayan geliştirme ortamı.

## LangChain'de Zincirlerin (Chains) Önemi

Zincirler, LLM'lerle etkileşimi daha yapılandırılmış ve verimli hale getirir. Basit bir zincir, bir istemin (prompt) hazırlanıp modele iletilmesi ve ardından modelin çıktısının alınması şeklinde olabilir. Daha karmaşık zincirler ise birden fazla model çağrısını, veri ön işleme adımlarını ve harici araçlarla entegrasyonları içerebilir. Bu yapı, geliştiricilere esneklik sağlar ve uygulamaların modülerliğini artırır. ​

## LangChain Kullanım Alanları

* Sohbet botları
* Belge özetleme
* Soru-cevap sistemleri
* Bilgiye dayalı karar verme sistemleri
* PDF, veritabanı, API ile çalışan yapılar

LangChain, geliştiricilere LLM tabanlı uygulamaları çok daha sistematik ve modüler şeklinde inşa etme fırsatı sunar. Hem akademik çalışmalarda hem de endüstriyel uygulamalarda yaygınlaşan bir altyapıdır.

## Zincir Türleri

1- **Basit Zincirler (Simple Chains):** Tek bir LLM çağrısını içerir. Örneğin, bir kullanıcının sorusunu alıp doğrudan modele ileterek yanıt almak.​
2- **Çok Adımlı Zincirler (Multi-Step Chains):** Birden fazla LLM çağrısını veya veri işleme adımını sıralı olarak uygular. Örneğin, önce bir soruyu yeniden ifade edip ardından modele iletmek.
3- Aracılı Zincirler (Agentic Chains): Modelin, belirli araçları kullanarak görevleri yerine getirdiği zincirlerdir. Bu tür zincirlerde model, hangi aracı kullanacağına karar verir ve gerekli eylemleri gerçekleştirir.


## Zincirlerin Kullanım Alanları

* **Soru-Cevap Sistemleri:** Kullanıcının sorusunu anlayıp, ilgili bilgiyi çekerek yanıt üretmek.​
* **Belge Özetleme:** Uzun metinleri kısaltarak önemli bilgileri öne çıkarmak.​
* **Veri Dönüştürme:** Verileri bir formattan diğerine dönüştürmek veya yapılandırmak.

## Pratik Örnek: Basit Bir Zincir Oluşturma

Aşağıdaki Python kodu, LangChain kullanarak basit bir zincir oluşturur. Bu zincir, verilen bir konu hakkında espri yapar:​

``` python
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import StrOutputParser

# İstem şablonu oluşturma
prompt = ChatPromptTemplate.from_template("{konu} hakkında bir espri yapar mısın?")

# LLM modeli seçimi
model = ChatOpenAI(model="gpt-3.5-turbo")

# Çıktı ayrıştırıcı
output_parser = StrOutputParser()

# Zinciri oluşturma
zincir = prompt | model | output_parser

# Zinciri çalıştırma
sonuc = zincir.invoke({"konu": "ayılar"})
print(sonuc)
```

LangChain'in zincir yapıları, geliştiricilere LLM tabanlı uygulamalarını daha etkili ve modüler bir şekilde tasarlama imkanı sunar. Bu sayede, karmaşık iş akışları daha yönetilebilir ve ölçeklenebilir hale gelir.​

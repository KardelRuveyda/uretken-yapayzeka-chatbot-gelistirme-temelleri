## Prompt nedir? 

 Prompt, en basit tanımıyla bir yapay zeka modeline verdiğiniz yazılı talimattır. Büyük dil modelleri, kendilerine yöneltilen sorular veya komutlar aracılığıyla cevap üretirler. Yani siz bir soru sorduğunuzda veya istekte bulunduğunuzda (prompt), model bu girdiye uygun bir yanıt vermeye çalışır. Örneğin, bir öğrenci **ChatGPT**'ye **"Merhaba, bana yapay zekanın ne olduğunu açıklar mısın?"** diye sorduğunda bu soru model için bir prompt olur ve ChatGPT buna yanıt üretir. Prompt'lar bir cümle, bir soru ya da çok daha detaylı yönergeler içerebilir.

## Prompt Engineering neden önemlidir?

ChatGPT’nin vereceği cevabın kalitesi, büyük ölçüde sizin nasıl bir prompt yazdığınıza bağlıdır. Doğru ve etkili bir prompt yazdığınızda modelin sizin istediğiniz sonuçları üretmesine yardımcı olursunuz​. Kötü yazılmış, belirsiz bir prompt ise modelin anlamsız veya alakasız yanıtlar vermesine yol açabilir. Bu nedenle, yapay zeka çağında **“Prompt Mühendisliği”** diye anılan bir yetkinlik ortaya çıkmıştır. Prompt mühendisliği, bir modelden istenen çıktıları almak için girdilerin (yani soruların/talimatların) dikkatli bir şekilde tasarlanması sürecidir. Başka bir deyişle, modelin daha doğru, anlamlı veya spesifik yanıtlar vermesini sağlamak için sorumuzu nasıl biçimlendireceğimizi bilmemiz gerekir. Özellikle sınavlara çalışırken, ChatGPT’den en verimli şekilde faydalanmak için iyi prompt yazma becerisi çok önemlidir.

## Doğru ve Etkili Prompt Yazmanın Kuralları

Büyük Dil Modellerinden en iyi şekilde faydalanmak için prompt yazarken bazı temel ilkelere dikkat etmek gerekir. İşte doğru ve etkili prompt yazmanın kuralları:

* **Açık ve spesifik olun**: İsteğinizi olabildiğince net ifade edin. Belirsiz veya çok genel sorular sormak yerine tam olarak ne öğrenmek istediğinizi belirtin. Örneğin, sadece "Bana sağlık hakkında bilgi ver" demek yerine, "Dengeli beslenme ve düzenli egzersizin sağlıklı yaşam tarzındaki rolünü açıkla" demek daha iyi sonuç verir​. Spesifik terimler ve hedefler kullanmak, modelin amacınızı doğru anlamasına yardımcı olur.
* **Bağlam sağlayın:** Sorunuz belli bir bağlam gerektiriyorsa onu prompt’unuza ekleyin. Ön bilgi, veri veya koşulları belirtmek, modelin daha alakalı yanıtlar üretmesini sağlar​. Örneğin, "Kripto para birimleri hakkında bilgi ver" yerine, "2021'den bu yana Bitcoin fiyatındaki dalgalanmaları ve nedenlerini analiz et" şeklinde sormak daha odaklı bir cevap getirir​. Benzer şekilde, kendi notlarınızdan özet istemeden önce notları veya konuyu kısaca tanıtabilirsiniz.
* **Adım adım yönlendirin:** Özellikle karmaşık sorunlarda, modelden adım adım düşünmesini isteyin. Bu yaklaşım, düşünce zinciri (chain-of-thought) tekniği olarak bilinir ve modelin çok adımlı bir problemde ara adımları da üretmesine yardımcı olur​ . Örneğin, "Bu matematik problemini çöz" demek yerine "Adım adım göstererek bu matematik problemini çözmeni istiyorum" diyebilirsiniz. Böylece ChatGPT, sonuca ulaşmadan önce her aşamayı açıklayarak ilerler. Örnek ve format verin: İstediğiniz çıktı biçimi belliyse bunu belirtin ve gerekiyorsa örnek ekleyin. Modelin nasıl bir yanıt üretmesini beklediğinizi göstermek, işi kolaylaştırır​. Örneğin, bir liste istiyorsanız "Listele: ..." diye başlamayı veya "her maddesi kısa cümlelerden oluşan bir liste hazırla" demeyi düşünebilirsiniz. Ya da "Cevabı üç paragrafta ver" gibi format belirtebilirsiniz. Örneğin: "Japonya'daki en popüler beş turistik yeri listele ve kısaca açıkla." şeklindeki bir prompt, paragraf paragraf genel bilgi istemekten daha yönlendiricidir​
* **Ton veya rol belirtin**: Cevabın resmi, samimi, teknik veya basit olmasını mı istiyorsunuz? Bunu açıkça dile getirin. Örneğin: "Basit bir dille açıkla:", "Resmi bir üslupla yanıtla:" ya da "Bir tarih öğretmeni gibi anlat:" gibi ifadeler kullanabilirsiniz​. Bu, modelin cevabının üslubunu beklentinize uygun hale getirir. Yaratıcı bir şey isterken de ton ve tarz belirtebilirsiniz (örn. masalsı, espirili, akademik vb. bir ton).
Uzunluk veya detay düzeyini ayarlayın: İstediğiniz cevabın ne kadar kapsamlı olacağını söylemekten çekinmeyin. Örneğin, "100 kelime ile özetle..." veya "Detaylı bir paragraf yaz..." gibi talimatlar verebilirsiniz​. Bu sayede ne kadar ayrıntı beklediğinizi model anlar. Kısa bir özet mi istiyorsunuz yoksa derinlemesine bir açıklama mı, bunu belirtmek faydalı olacaktır.
* **Kompleks istekleri parçalara bölün:** Bir seferde çok fazla şey istemek yerine, sorularınızı gerektiğinde bölerek sorun. Eğer kapsamlı bir konuyu çalışıyorsanız, önce alt başlıkları ayrı ayrı sormak sonra bunları derlemek daha iyi sonuç verebilir. Örneğin, uzun bir metni özetletip sonra önemli noktaları ayrı bir prompt ile sorgulayabilirsiniz. Bu yaklaşım, token sınırına takılmadan büyük görevleri yönetilebilir parçalara ayırmanıza da yardımcı olur​.
* **Yanıtları yineleyerek iyileştirin:** ChatGPT ile etkileşim tek seferlik olmak zorunda değil. İlk aldığınız yanıt tam istediğiniz gibi olmayabilir. Bu durumda prompt’unuzu yineleyin veya modeli verdiği cevap üzerinden yönlendirin​. Örneğin, "Daha basit açıklayabilir misin?" veya "Bu cevabı maddeler halinde yeniden yazar mısın?" diyerek cevabın biçimini veya içeriğini geliştirebilirsiniz. Bu tür çok turlu diyalog, nihai olarak daha tatmin edici bir sonuç almanızı sağlar.

Yukarıdaki kuralları uyguladıkça, Büyük Dil Modelleri’nin size verdiği yanıtların kalitesinin arttığını göreceksiniz. Özetle, ne sorduğunuz, nasıl sorduğunuza bağlıdır. Şimdi, iyi ve kötü yazılmış prompt’ların bazı örneklerine bakalım.

## İyi ve Kötü Prompt Örnekleri (Karşılaştırmalı)

Aşağıda, aynı konu için yazılmış kötü ve iyi prompt örneklerini karşılaştırmalı olarak görebilirsiniz. Kötü örneklerde sorular genellikle çok genel, belirsiz veya yetersiz iken, iyi örnekler daha net, yönlendirici ve amaca uygun şekilde yazılmıştır:

**Kötü:** "Sağlıklı yaşam hakkında bilgi ver." <br/>(Çok genel bir istek; hangi yönüyle sağlıklı yaşam?)
**İyi:** "Öner: Dengeli beslenme, düzenli egzersiz ve yeterli uykunun sağlıklı yaşam tarzını sürdürmedeki rolünü açıkla." <br/>(Belirli unsurları vurgulayarak sağlıklı yaşamın üç temel unsurunu açıkla talebi)

**Kötü**: "Özetle: Renklerin insan psikolojisi üzerindeki genel etkilerini ve özellikle mavi rengin sakinleştirici etkisine dair bilimsel kanıtları sun." <br/>(Hangi konuda özet istendiği ve özel bir vurguyla belirtilmiş)​
**İyi:** "Renkler ve psikoloji." <br/>(Ne isteniyor belli değil; renklerin psikolojiyle ilişkisi mi?)

**Kötü:** "Kripto para birimleri." <br/>(Çok geniş bir konu, spesifik değil)
**İyi:**  "Analiz et: 2021'den bu yana Bitcoin'in fiyat dalgalanmalarını ve bu dalgalanmaların olası nedenlerini incele." <br/>(Belirli bir zaman aralığı ve içerik isteyerek daha odaklı bir analiz talebi)​

**Kötü:** "Photoshop'ta katmanlar." <br/>(Soru mu, istek mi? Konu belirsiz)
**İyi:**  "Kısa özet yaz: Photoshop'taki katmanların temel işlevlerini 100 kelimeyle açıkla." <br/>(Hangi konuda, ne formatta ve ne uzunlukta cevap istendiği belirtilmiş)​

Yukarıdaki örneklerde görüldüğü gibi, kötü promptlar kısa ve belirsiz olup modelin hangi yönde cevap vermesi gerektiğini açıkça belirtmiyor. Oysa iyi promptlar yönerge, bağlam ve ayrıntı vererek modelin işini kolaylaştırıyor. 

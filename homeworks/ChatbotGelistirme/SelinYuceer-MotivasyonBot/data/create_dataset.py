import pandas as pd
import random

def create_motivasyon_dataset():
    """
    7 farklı intent için toplam 1000 cümle oluşturur
    Her intent için yaklaşık 143 cümle
    """
    
    # Intent'ler ve örnek cümleler
    intents_data = {
        'motivasyon_sozu': [
            "Bugün kendime nasıl motivasyon verebilirim?",
            "Bana güçlü hissettiren bir söz söyler misin?",
            "Hayatımda ilerleme kaydetmek istiyorum",
            "Başarı için ne yapmalıyım?",
            "Kendime güvenmeyi öğrenmek istiyorum",
            "Güçlü olmak için ne yapabilirim?",
            "Hayallerimi gerçekleştirmek istiyorum",
            "Zorlukları aşmak için ne yapmalıyım?",
            "Pozitif düşünmek istiyorum",
            "Kendimi geliştirmek istiyorum",
            "İlham verici bir söz duyabilir miyim?",
            "Umut dolu bir mesaj alabilir miyim?",
            "Cesaretimi toplamak istiyorum",
            "Kendimi motive etmek istiyorum",
            "Güçlü kalmaya ihtiyacım var",
            "Başarıya odaklanmak istiyorum",
            "Hedeflerime ulaşmak istiyorum",
            "Kararlı olmayı öğrenmek istiyorum",
            "Sabırlı olmak istiyorum",
            "Azimli olmaya ihtiyacım var"
        ],
        
        'kötü_gün_destek': [
            "Bugün çok kötü hissediyorum",
            "Moralim bozuk, yardım et",
            "Her şey ters gidiyor",
            "Umutsuzluğa kapıldım",
            "Kendimi berbat hissediyorum",
            "Hiçbir şey istediğim gibi gitmiyor",
            "Çok üzgünüm",
            "Stresli bir gün geçiriyorum",
            "Karamsar hissediyorum",
            "Mutsuzum",
            "Her şey çok zor geliyor",
            "Yorgunum ve bitkinim",
            "Hayal kırıklığına uğradım",
            "Kötü bir gün geçiriyorum",
            "Moralsizim",
            "Hüzünlüyüm",
            "Kederli hissediyorum",
            "Üzgün bir ruh halindeyim",
            "Boş hissediyorum",
            "Motivasyonum yok"
        ],
        
        'hedef_önerisi': [
            "Yeni hedefler belirlemek istiyorum",
            "Hayatımda ne yapabilirim?",
            "Hangi amaçları güdmeliyim?",
            "Kendimi geliştirmek için ne yapabilirim?",
            "Yeni bir hobi edinmek istiyorum",
            "Becerilerimi geliştirmek istiyorum",
            "Kişisel gelişim için öneriler ver",
            "Yeni bir şey öğrenmek istiyorum",
            "Kariyerimde ilerleme kaydetmek istiyorum",
            "Sosyal hayatımı geliştirmek istiyorum",
            "Daha üretken olmak istiyorum",
            "Zamanımı daha iyi değerlendirmek istiyorum",
            "Yeni alışkanlıklar edinmek istiyorum",
            "Sağlıklı yaşam için ne yapabilirim?",
            "Mutluluk için hedefler belirlemek istiyorum",
            "Başarılı olmak için planlar yapmak istiyorum",
            "Hayallerimi gerçekleştirmek için ne yapmalıyım?",
            "Gelecek planlarım neler olabilir?",
            "Kendimi motive edecek amaçlar arıyorum",
            "Yaşam kalitemi artırmak istiyorum"
        ],
        
        'meditasyon_önermesi': [
            "Zihnimin sakinleşmesine ihtiyacım var",
            "Stresimi azaltmak istiyorum",
            "Rahatlamak istiyorum",
            "Zihinsel huzur arıyorum",
            "Meditasyon yapmak istiyorum",
            "Sakinleşmek istiyorum",
            "İç huzuru bulmak istiyorum",
            "Zihnimin durulmasını istiyorum",
            "Relaksasyon teknikleri öğrenmek istiyorum",
            "Nefes egzersizleri yapabilir miyim?",
            "Huzurlu hissetmek istiyorum",
            "Gerginliğimi atmak istiyorum",
            "Zihnimde rahatlık istiyorum",
            "Sakinlik arıyorum",
            "Endişelerimi yatıştırmak istiyorum",
            "Zihinsel dinginlik istiyorum",
            "Meditasyon rehberliği alabilir miyim?",
            "Ruhsal huzur arıyorum",
            "Zihinsel berraklık istiyorum",
            "Sakin kalmayı öğrenmek istiyorum"
        ],
        
        'selamlaşma': [
            "Merhaba",
            "Selam",
            "İyi günler",
            "Günaydın",
            "İyi akşamlar",
            "Hey",
            "Nasılsın?",
            "Selamlar",
            "Hoş geldin",
            "Merhaba chatbot",
            "Selam nasılsın?",
            "İyi günler nasıl gidiyor?",
            "Herkese selam",
            "Selamün aleyküm",
            "İyi sabahlar",
            "Günaydın çiçeğim",
            "Selam canım",
            "Merhabalar",
            "Selamlar herkese",
            "Hoşgeldiniz"
        ],
        
        'vedalaşma': [
            "Görüşürüz",
            "Hoşçakal",
            "İyi günler",
            "Bye",
            "Güle güle",
            "Kendine iyi bak",
            "Başka zaman görüşürüz",
            "Hoşçakal dostum",
            "İyi akşamlar",
            "İyi geceler",
            "Sonra görüşürüz",
            "Elveda",
            "Güle güle kal",
            "Hoşçakal canım",
            "Çok teşekkürler hoşçakal",
            "Sağlıcakla kal",
            "Kendine dikkat et",
            "Mutlu günler",
            "Hoşçakal kardeşim",
            "Bay bay"
        ],
        
        'spor_önerisi': [
            "Egzersiz yapmak istiyorum",
            "Spor yapmaya başlamak istiyorum",
            "Fitness önerileri ver",
            "Hangi sporu yapabilirim?",
            "Fiziksel aktivite önerileri",
            "Evde spor yapabilir miyim?",
            "Antrenman programı istiyorum",
            "Sağlıklı olmak için ne yapabilirim?",
            "Kilo vermek istiyorum",
            "Kondisyon yapmak istiyorum",
            "Jimnastik hareketleri öğrenmek istiyorum",
            "Yürüyüş yapmak istiyorum",
            "Koşu yapmaya başlamak istiyorum",
            "Yoga yapmak istiyorum",
            "Pilates yapmak istiyorum",
            "Kas yapmak istiyorum",
            "Stretching yapmak istiyorum",
            "Kardiyo egzersizleri yapmak istiyorum",
            "Güçlü olmak için ne yapabilirim?",
            "Fiziksel olarak aktif olmak istiyorum"
        ]
    }
    
    # Her intent için cümle sayısını artır
    expanded_data = []
    target_per_intent = 143
    
    for intent, base_sentences in intents_data.items():
        sentences = base_sentences.copy()
        
        # Cümleleri çeşitlendirme
        variations = []
        for sentence in base_sentences:
            # Farklı varyasyonlar ekle
            variations.extend([
                sentence,
                sentence.replace("istiyorum", "istiyordum"),
                sentence.replace("miyim", "miyiz"),
                sentence.replace("?", "."),
                sentence + " lütfen",
                sentence.replace("bana", "bize"),
            ])
        
        # Hedef sayıya ulaşana kadar rastgele seç
        while len(sentences) < target_per_intent:
            sentences.append(random.choice(variations))
        
        # Hedef sayıya tam olarak ulaş
        sentences = sentences[:target_per_intent]
        
        # Veri setine ekle
        for sentence in sentences:
            expanded_data.append({
                'Intent': intent,
                'Sentence': sentence
            })
    
    # DataFrame oluştur
    df = pd.DataFrame(expanded_data)
    
    # Karıştır
    df = df.sample(frac=1).reset_index(drop=True)
    
    print(f"Toplam cümle sayısı: {len(df)}")
    print("\nIntent dağılımı:")
    print(df['Intent'].value_counts())
    
    return df

if __name__ == "__main__":
    # Veri setini oluştur
    dataset = create_motivasyon_dataset()
    
    # Excel dosyası olarak kaydet
    dataset.to_excel('data/chatbot_dataset.xlsx', index=False)
    
    # CSV olarak da kaydet
    dataset.to_csv('data/chatbot_dataset.csv', index=False, encoding='utf-8')
    
    print("\nVeri seti başarıyla oluşturuldu!")
    print("Dosyalar: chatbot_dataset.xlsx ve chatbot_dataset.csv") 
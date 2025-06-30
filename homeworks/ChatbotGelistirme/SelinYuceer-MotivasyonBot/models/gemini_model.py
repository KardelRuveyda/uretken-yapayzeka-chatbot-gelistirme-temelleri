import google.generativeai as genai
import pandas as pd
import time
from typing import List, Dict, Tuple
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, classification_report

class GeminiIntentClassifier:
    """
    Google Gemini kullanarak intent sınıflandırması yapan sınıf
    """
    
    def __init__(self, api_key: str = None):
        """
        Gemini Intent Classifier'ı başlatır
        
        Args:
            api_key (str): Google AI API anahtarı
        """
        if api_key:
            genai.configure(api_key=api_key)
        else:
            # Çevre değişkeninden API anahtarını al
            api_key = os.getenv('GOOGLE_API_KEY')
            if api_key:
                genai.configure(api_key=api_key)
        
        # Intent kategorileri ve açıklamaları
        self.intent_descriptions = {
            'motivasyon_sozu': 'Kullanıcı motivasyon, ilham verici sözler veya cesaret verici mesajlar istiyor',
            'kötü_gün_destek': 'Kullanıcı kötü bir gün geçiriyor, morali bozuk veya destek istiyor',
            'hedef_önerisi': 'Kullanıcı yeni hedefler, amaçlar veya kişisel gelişim önerileri istiyor',
            'meditasyon_önermesi': 'Kullanıcı sakinleşmek, rahatlamak veya meditasyon tekniği istiyor',
            'selamlaşma': 'Kullanıcı selamlaşma, merhaba deme veya konuşmaya başlama',
            'vedalaşma': 'Kullanıcı vedalaşma, görüşürüz deme veya konuşmayı bitirme',
            'spor_önerisi': 'Kullanıcı egzersiz, spor, fitness veya fiziksel aktivite önerisi istiyor'
        }
        
        # Model yapılandırması
        self.generation_config = {
            "temperature": 0.1,
            "top_p": 0.95,
            "top_k": 40,
            "max_output_tokens": 50,
        }
        
        self.safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        ]
        
        try:
            self.model = genai.GenerativeModel(
                model_name="gemini-1.5-flash",
                generation_config=self.generation_config,
                safety_settings=self.safety_settings
            )
        except Exception as e:
            print(f"Model oluşturma hatası: {e}")
            self.model = None
    
    def create_prompt(self, text: str) -> str:
        """
        Gemini için prompt oluşturur
        
        Args:
            text (str): Sınıflandırılacak metin
            
        Returns:
            str: Gemini için hazırlanmış prompt
        """
        intent_list = "\n".join([f"- {intent}: {desc}" for intent, desc in self.intent_descriptions.items()])
        
        prompt = f"""Sen bir metin sınıflandırma uzmanısın. Aşağıdaki Türkçe metni analiz et ve hangi kategoriye ait olduğunu belirle.

Kategoriler:
{intent_list}

Analiz edilecek metin: "{text}"

SADECE kategori adını döndür (örnek: motivasyon_sozu). Hiçbir açıklama yapma, sadece kategori adı!"""
        
        return prompt
    
    def predict_single(self, text: str) -> str:
        """
        Tek bir metin için intent tahmini yapar
        
        Args:
            text (str): Sınıflandırılacak metin
            
        Returns:
            str: Tahmin edilen intent
        """
        if not self.model:
            return 'motivasyon_sozu'  # Varsayılan
            
        try:
            prompt = self.create_prompt(text)
            response = self.model.generate_content(prompt)
            
            if response.text:
                prediction = response.text.strip().lower()
                
                # Geçerli intent kontrolü
                if prediction in self.intent_descriptions.keys():
                    return prediction
                else:
                    # En yakın intent'i bul
                    for intent in self.intent_descriptions.keys():
                        if intent in prediction or prediction in intent:
                            return intent
                    return 'motivasyon_sozu'  # Varsayılan
            else:
                return 'motivasyon_sozu'  # Varsayılan
                
        except Exception as e:
            print(f"Tahmin hatası: {e}")
            return 'motivasyon_sozu'  # Varsayılan intent
    
    def predict_batch(self, texts: List[str], delay: float = 1.0) -> List[str]:
        """
        Bir metin listesi için intent tahminleri yapar
        
        Args:
            texts (List[str]): Sınıflandırılacak metinler
            delay (float): API çağrıları arası bekleme süresi (saniye)
            
        Returns:
            List[str]: Tahmin edilen intent'ler
        """
        predictions = []
        
        for i, text in enumerate(texts):
            if i > 0:
                time.sleep(delay)  # Rate limiting için bekleme
            
            prediction = self.predict_single(text)
            predictions.append(prediction)
            
            if (i + 1) % 10 == 0:
                print(f"İşlenen: {i + 1}/{len(texts)}")
        
        return predictions
    
    def evaluate_model(self, test_texts: List[str], true_labels: List[str]) -> Dict:
        """
        Model performansını değerlendirir
        
        Args:
            test_texts (List[str]): Test metinleri
            true_labels (List[str]): Gerçek etiketler
            
        Returns:
            Dict: Performans metrikleri
        """
        print("Gemini model değerlendirmesi başlıyor...")
        
        # Tahminleri al
        predictions = self.predict_batch(test_texts, delay=0.5)
        
        # Metrikleri hesapla
        accuracy = accuracy_score(true_labels, predictions)
        precision, recall, f1, support = precision_recall_fscore_support(
            true_labels, predictions, average='weighted'
        )
        
        # Detaylı rapor
        report = classification_report(true_labels, predictions, output_dict=True)
        
        results = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'detailed_report': report,
            'predictions': predictions
        }
        
        return results

    def get_motivation_response(self, intent: str) -> str:
        """
        Intent'e göre motivasyon mesajı döndürür
        
        Args:
            intent (str): Tespit edilen intent
            
        Returns:
            str: Motivasyon mesajı
        """
        responses = {
            'motivasyon_sozu': [
                "💪 Hayatın en büyük zaferleri, pes etmemeyi seçtiğin anlarda başlar!",
                "🌟 Sen her zorluğun üstesinden gelebilecek güçtesin! İnan kendine!",
                "🚀 Başarı, küçük adımların büyük bir toplamıdır. Devam et!",
                "✨ Bugün kendine yatırım yapabileceğin harika bir gün!",
                "🎯 Hedeflerine odaklan, engeller sadece geçicidir!"
            ],
            'kötü_gün_destek': [
                "🤗 Her fırtınadan sonra güneş çıkar. Bu zor anlar da geçecek, güçlü kalıyorsun!",
                "💙 Bugün zor bir gün ama sen daha zor günleri de atlattın. Bu da geçecek!",
                "🌈 Kötü günler, iyi günlerin değerini anlamamızı sağlar. Yarın daha güzel olacak!",
                "🫂 Kendine karşı nazik ol. Zor zamanlar geçici, sen kalıcısın!",
                "🌱 En güzel çiçekler en zor koşullarda büyür. Sen de güçlü çıkacaksın bundan!"
            ],
            'hedef_önerisi': [
                "📚 Bugün yeni bir beceri öğrenmeye ne dersin? Küçük adımlarla başla!",
                "🏃‍♀️ Günde 10 dakika yürüyüş yapmayı hedefleyebilirsin.",
                "📖 Her gün 5 sayfa kitap okumak harika bir başlangıç olabilir!",
                "🧘‍♀️ Günlük 5 dakika meditasyon yapmayı deneyebilirsin.",
                "💧 Günde 8 bardak su içmeyi hedefle, vücudun teşekkür edecek!"
            ],
            'meditasyon_önermesi': [
                "🧘‍♀️ Derin bir nefes al... Burnundan 4 sayarak içeri, ağzından 6 sayarak dışarı ver.",
                "🌊 Gözlerini kapa ve dalgaların sesini hayal et. 5 dakika sadece nefesine odaklan.",
                "🍃 Şu anda burada olduğunu hisset. Ayaklarını yere değdirip köklendiklerini hayal et.",
                "☁️ Düşüncelerinin bulut gibi gelip geçmesine izin ver. Sen sadece izleyicisin.",
                "🌸 Kalbinin atışlarını hisset. Bu ritim seni sakinleştirecek."
            ],
            'selamlaşma': [
                "👋 Merhaba! Bugün seni nasıl motive edebilirim?",
                "🌟 Selam! Harika şeyler yapmaya hazır mısın?",
                "😊 Hey! Bugün senin günün, harika geçsin!",
                "🎉 Merhaba! Yeni bir gün, yeni fırsatlar!",
                "💫 Selam! Bugün kendine nasıl iyilik yapacaksın?"
            ],
            'vedalaşma': [
                "👋 Görüşürüz! Unutma, sen harikasın!",
                "🌟 Hoşçakal! Bugün kendine gururla bakabilirsin!",
                "💪 Güle güle! Yarın daha da güçlü olacaksın!",
                "✨ Kendine iyi bak! Sen çok değerlisin!",
                "🎯 Hoşçakal! Hedeflerine doğru emin adımlarla yürü!"
            ],
            'spor_önerisi': [
                "🏃‍♀️ 15 dakikalık tempolu yürüyüş başlamak için mükemmel!",
                "💪 Evde 10 şınav, 10 mekik ile güne başlayabilirsin!",
                "🧘‍♀️ Yoga videolarıyla esnekliğini artırabilirsin.",
                "🏊‍♀️ Haftada 2-3 kez havuz keyifli bir aktivite olabilir!",
                "🚴‍♀️ Bisiklet sürmek hem eğlenceli hem sağlıklı!"
            ]
        }
        
        import random
        if intent in responses:
            return random.choice(responses[intent])
        else:
            return random.choice(responses['motivasyon_sozu'])

def load_and_prepare_data(data_path: str) -> Tuple[List[str], List[str], List[str], List[str]]:
    """
    Veri setini yükler ve eğitim/test olarak böler
    
    Args:
        data_path (str): Veri dosyasının yolu
        
    Returns:
        Tuple: (X_train, X_test, y_train, y_test)
    """
    # Veri setini yükle
    if data_path.endswith('.xlsx'):
        df = pd.read_excel(data_path)
    else:
        df = pd.read_csv(data_path)
    
    # Eğitim ve test olarak böl (%80 - %20)
    X_train, X_test, y_train, y_test = train_test_split(
        df['Sentence'].tolist(),
        df['Intent'].tolist(),
        test_size=0.2,
        random_state=42,
        stratify=df['Intent']
    )
    
    return X_train, X_test, y_train, y_test

def main():
    """
    Ana fonksiyon - model testi
    """
    print("🤖 Gemini Motivasyon Chatbot Modeli Test Ediliyor...")
    
    # Veriyi yükle
    data_path = 'data/chatbot_dataset.csv'
    X_train, X_test, y_train, y_test = load_and_prepare_data(data_path)
    
    print(f"📊 Eğitim seti boyutu: {len(X_train)}")
    print(f"📊 Test seti boyutu: {len(X_test)}")
    
    # Classifier oluştur
    classifier = GeminiIntentClassifier()
    
    # Örnek tahminler
    sample_texts = [
        "Bugün kendimi çok kötü hissediyorum",
        "Bana motivasyon verici bir söz söyler misin?",
        "Merhaba",
        "Spor yapmak istiyorum",
        "Sakinleşmek istiyorum",
        "Görüşürüz"
    ]
    
    print("\n🔍 Örnek Tahminler:")
    print("-" * 50)
    
    for text in sample_texts:
        try:
            intent = classifier.predict_single(text)
            response = classifier.get_motivation_response(intent)
            print(f"💬 Metin: {text}")
            print(f"🎯 Intent: {intent}")
            print(f"💡 Cevap: {response}")
            print("-" * 50)
        except Exception as e:
            print(f"❌ Hata: {text} -> {e}")
    
    print("\n✅ Test tamamlandı!")
    print("📝 Not: Gerçek API anahtarı ile daha detaylı test yapabilirsiniz.")
    print("🔑 API anahtarını GOOGLE_API_KEY çevre değişkeni olarak ayarlayın.")

if __name__ == "__main__":
    main() 
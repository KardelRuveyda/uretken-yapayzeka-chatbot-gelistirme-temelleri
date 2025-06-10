import openai
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
)
import json
import os
from typing import List, Dict, Tuple
from dotenv import load_dotenv

# Çevre değişkenlerini yükle
load_dotenv()


class GPTChatbot:
    """OpenAI GPT tabanlı Türk mutfağı chatbot sınıfı"""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OpenAI API anahtarı gerekli. Lütfen .env dosyasında OPENAI_API_KEY değerini ayarlayın."
            )

        openai.api_key = self.api_key
        self.client = openai.OpenAI(api_key=self.api_key)

        self.intent_examples = {
            "greeting": ["Merhaba", "Selam", "İyi günler", "Hoş geldiniz", "Günaydın"],
            "goodbye": ["Görüşürüz", "Hoşçakal", "İyi günler", "Elveda", "Güle güle"],
            "recipe_request": [
                "Döner nasıl yapılır?",
                "Lahmacun tarifi verir misin?",
                "Baklava nasıl yapılır?",
                "Köfte tarifi",
                "Pilav nasıl pişirilir?",
            ],
            "ingredient_query": [
                "Döner hangi malzemelerle yapılır?",
                "Lahmacun için ne gerekir?",
                "Baklava malzemeleri neler?",
                "Kebab için hangi baharat kullanılır?",
                "Pilav malzemeleri",
            ],
            "cooking_technique": [
                "Et nasıl marine edilir?",
                "Soğan kavurma tekniği",
                "Hamur açma tekniği",
                "Kızartma sıcaklığı",
                "Pişirme süresi nasıl hesaplanır?",
            ],
            "nutrition_info": [
                "Döner kalorisi",
                "Lahmacun besin değeri",
                "Baklava şeker oranı",
                "Kebab protein miktarı",
                "Pilav karbonhidrat",
            ],
            "menu_suggestion": [
                "Bugün ne yemek yapalım?",
                "Haftalık menü önerisi",
                "Misafir menüsü",
                "Diet menü önerisi",
                "Ekonomik menü",
            ],
            "rejection": [
                "Anlamadım",
                "Ne demek istiyorsun?",
                "Bu konuda bilgim yok",
                "Başka bir şey sormak ister misin?",
                "Türk mutfağı hakkında konuşalım",
            ],
        }

        self.recipe_database = {
            "döner": {
                "malzemeler": [
                    "Et (kuzu/tavuk)",
                    "Soğan",
                    "Domates",
                    "Baharat karışımı",
                    "Yoğurt",
                    "Lavash",
                ],
                "tarif": "1. Eti ince dilimle. 2. Baharatlarla marine et. 3. Şişe diz. 4. Döndürerek pişir.",
                "süre": "2-3 saat",
                "kalori": "250-300 kalori/porsiyon",
            },
            "lahmacun": {
                "malzemeler": [
                    "İnce hamur",
                    "Kıyma",
                    "Soğan",
                    "Domates",
                    "Maydanoz",
                    "Baharat",
                ],
                "tarif": "1. Hamuru aç. 2. Kıyma harcını hazırla. 3. Hamur üzerine yay. 4. Fırında pişir.",
                "süre": "30-45 dakika",
                "kalori": "200-250 kalori/adet",
            },
            "baklava": {
                "malzemeler": [
                    "Yufka",
                    "Ceviz/Fıstık",
                    "Tereyağı",
                    "Şerbet (şeker, su, limon)",
                ],
                "tarif": "1. Yufkaları yağla. 2. Ceviz serp. 3. Katla ve kes. 4. Fırında pişir. 5. Şerbet dök.",
                "süre": "1-2 saat",
                "kalori": "300-400 kalori/parça",
            },
            "köfte": {
                "malzemeler": ["Kıyma", "Soğan", "Ekmek içi", "Yumurta", "Baharat"],
                "tarif": "1. Malzemeleri karıştır. 2. Köfte şekli ver. 3. Tavada veya ızgarada pişir.",
                "süre": "30 dakika",
                "kalori": "150-200 kalori/adet",
            },
            "pilav": {
                "malzemeler": ["Pirinç", "Su/Et suyu", "Tereyağı", "Tuz"],
                "tarif": "1. Pirinci kavur. 2. Sıcak su ekle. 3. Kaynatıp kısık ateşte pişir.",
                "süre": "25-30 dakika",
                "kalori": "180-220 kalori/porsiyon",
            },
        }

    def classify_intent(self, text: str) -> str:
        """Metin için intent sınıflandırması yap"""
        # Basit kelime eşleştirme ile intent belirleme
        text = text.lower()
        
        # Greeting kontrolü
        if any(word in text for word in ["merhaba", "selam", "günaydın", "iyi günler"]):
            return "greeting"
            
        # Goodbye kontrolü
        if any(word in text for word in ["hoşçakal", "görüşürüz", "güle güle"]):
            return "goodbye"
            
        # Recipe request kontrolü
        if any(word in text for word in ["nasıl yapılır", "tarifi", "yapılışı", "tarif"]):
            return "recipe_request"
            
        # Ingredient query kontrolü
        if any(word in text for word in ["malzemeler", "içindekiler", "gerekli malzemeler"]):
            return "ingredient_query"
            
        # Cooking technique kontrolü
        if any(word in text for word in ["teknik", "nasıl pişirilir", "pişirme"]):
            return "cooking_technique"
            
        # Nutrition info kontrolü
        if any(word in text for word in ["kalori", "besin değeri", "protein", "karbonhidrat"]):
            return "nutrition_info"
            
        # Menu suggestion kontrolü
        if any(word in text for word in ["ne yapalım", "menü", "öneri"]):
            return "menu_suggestion"
            
        # Eğer hiçbir intent eşleşmezse
        return "rejection"

    def generate_response(self, text: str, intent: str) -> str:
        """Intent'e göre uygun yanıt oluştur"""

        if intent == "greeting":
            return "Merhaba! Türk mutfağı hakkında size nasıl yardımcı olabilirim? Yemek tarifleri, malzemeler veya pişirme teknikleri hakkında sorularınızı sorabilirsiniz."

        elif intent == "goodbye":
            return "Hoşçakalın! Türk mutfağı ile ilgili sorularınız olduğunda tekrar gelin. Afiyet olsun! 👋"

        elif intent == "recipe_request":
            # Yemek adını çıkarmaya çalış
            food_found = None
            for food in self.recipe_database.keys():
                if food.lower() in text.lower():
                    food_found = food
                    break

            if food_found:
                recipe = self.recipe_database[food_found]
                response = f"**{food_found.upper()} TARİFİ:**\n\n"
                response += f"🥘 **Malzemeler:** {', '.join(recipe['malzemeler'])}\n\n"
                response += f"👨‍🍳 **Yapılışı:** {recipe['tarif']}\n\n"
                response += f"⏰ **Süre:** {recipe['süre']}\n\n"
                response += f"📊 **Kalori:** {recipe['kalori']}"
                return response
            else:
                return self._get_general_recipe_help(text)

        elif intent == "ingredient_query":
            food_found = None
            for food in self.recipe_database.keys():
                if food.lower() in text.lower():
                    food_found = food
                    break

            if food_found:
                ingredients = self.recipe_database[food_found]["malzemeler"]
                return f"**{food_found.upper()} MALZEMELERİ:**\n\n🛒 {', '.join(ingredients)}"
            else:
                return "Hangi yemeğin malzemelerini öğrenmek istiyorsunuz? Döner, lahmacun, baklava, köfte veya pilav gibi yemeklerin malzemelerini söyleyebilirim."

        elif intent == "nutrition_info":
            food_found = None
            for food in self.recipe_database.keys():
                if food.lower() in text.lower():
                    food_found = food
                    break

            if food_found:
                calories = self.recipe_database[food_found]["kalori"]
                return f"**{food_found.upper()} BESİN BİLGİSİ:**\n\n📊 **Kalori:** {calories}\n\nDetaylı besin analizi için beslenme uzmanına danışmanızı öneririm."
            else:
                return "Hangi yemeğin besin değerlerini öğrenmek istiyorsunuz? Size kalori bilgilerini verebilirim."

        elif intent == "cooking_technique":
            return self._get_cooking_technique_advice(text)

        elif intent == "menu_suggestion":
            return self._get_menu_suggestion(text)

        else:  # rejection
            return "Üzgünüm, bu konuda size yardımcı olamam. Türk mutfağı, yemek tarifleri, malzemeler veya pişirme teknikleri hakkında sorularınızı yanıtlayabilirim. Ne yapmak istediğinizi sorabilir misiniz?"

    def _get_general_recipe_help(self, text: str) -> str:
        """Genel tarif yardımı"""
        prompt = f"""
        Türk mutfağı uzmanı olarak, aşağıdaki soruya kısa ve net bir tarif yanıtı ver.
        Sadece malzemeler ve temel yapılış adımlarını söyle.
        
        Soru: {text}
        
        Yanıt:"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "Sen Türk mutfağı uzmanısın. Kısa ve net tarifler veriyorsun.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=300,
            )

            return response.choices[0].message.content.strip()
        except Exception as e:
            return "Tarif konusunda şu an yardımcı olamıyorum. Lütfen daha sonra tekrar deneyin."

    def _get_cooking_technique_advice(self, text: str) -> str:
        """Pişirme tekniği tavsiyeleri"""
        techniques = {
            "marine": "Et marinesi için yoğurt, limon suyu ve baharatları karıştırın. En az 2 saat bekletin.",
            "kavurma": "Soğanları orta ateşte, şeffaf olana kadar kavurun. Acele etmeyin.",
            "hamur": "Hamuru açarken bol un kullanın ve yavaş çalışın. Dinlendirmeyi unutmayın.",
            "kızartma": "Yağ sıcaklığı 170-180°C olmalı. Ağızlı kabı kullanmayın.",
            "pişirme": "Düşük ateşte yavaş pişirme lezzeti artırır.",
        }

        for key, advice in techniques.items():
            if key in text.lower():
                return f"🧑‍🍳 **PİŞİRME TEKNİĞİ:**\n\n{advice}"

        return "🧑‍🍳 **GENEL PİŞİRME İPUÇLARI:**\n\n• Malzemeleri önceden hazırlayın\n• Ateş kontrolüne dikkat edin\n• Tadımları ihmal etmeyin\n• Sabırlı olun"

    def _get_menu_suggestion(self, text: str) -> str:
        """Menü önerileri"""
        if "kahvaltı" in text.lower():
            return "🌅 **KAHVALTI MENÜSÜ:**\n\n• Menemen\n• Simit & Peynir\n• Çay\n• Reçel & Bal"
        elif "akşam" in text.lower() or "iftar" in text.lower():
            return "🌙 **AKŞAM YEMEĞİ MENÜSÜ:**\n\n• Mercimek Çorbası\n• Kebab\n• Pilav\n• Salata\n• Baklava"
        elif "misafir" in text.lower():
            return "👥 **MİSAFİR MENÜSÜ:**\n\n• Çorba\n• Dolma & Sarma\n• Et Yemeği\n• Pilav\n• Tatlı\n• Türk Kahvesi"
        else:
            return "🍽️ **GÜNLÜK MENÜ ÖNERİSİ:**\n\n• Öğle: Köfte & Pilav\n• Akşam: Tavuk Şiş & Salata\n• Tatlı: Sütlaç"

    def evaluate_model(self, test_data: pd.DataFrame) -> Dict:
        """Model performansını değerlendir"""
        y_true = []
        y_pred = []

        print("Model değerlendirmesi başlıyor...")

        for idx, row in test_data.iterrows():
            if idx % 50 == 0:
                print(f"İşlenen: {idx}/{len(test_data)}")

            text = row["Örnek Cümle"]
            true_intent = row["Intent"]
            predicted_intent = self.classify_intent(text)

            y_true.append(true_intent)
            y_pred.append(predicted_intent)

        # Metrikleri hesapla
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred, average="weighted", zero_division=0)
        recall = recall_score(y_true, y_pred, average="weighted", zero_division=0)
        f1 = f1_score(y_true, y_pred, average="weighted", zero_division=0)

        results = {
            "model": "GPT-3.5-turbo",
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "predictions": list(zip(y_true, y_pred)),
        }

        print(f"\n🤖 GPT Model Performansı:")
        print(f"Accuracy: {accuracy:.3f}")
        print(f"Precision: {precision:.3f}")
        print(f"Recall: {recall:.3f}")
        print(f"F1 Score: {f1:.3f}")

        return results

    def chat(self, message: str) -> str:
        """Ana chat fonksiyonu"""
        intent = self.classify_intent(message)
        response = self.generate_response(message, intent)
        return response


if __name__ == "__main__":
    # Test için basit örnek
    try:
        chatbot = GPTChatbot()

        # Test mesajları
        test_messages = [
            "Merhaba",
            "Döner nasıl yapılır?",
            "Baklava malzemeleri neler?",
            "Hoşçakal",
        ]

        for msg in test_messages:
            print(f"Kullanıcı: {msg}")
            response = chatbot.chat(msg)
            print(f"Bot: {response}\n")

    except ValueError as e:
        print(f"Hata: {e}")
        print("Lütfen .env dosyasında OPENAI_API_KEY değerini ayarlayın.")

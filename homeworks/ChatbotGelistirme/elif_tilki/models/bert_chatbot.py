# ✅ Gerekli Kütüphaneleri İçe Aktar
import pandas as pd
import torch
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments, EarlyStoppingCallback
from torch.utils.data import Dataset

# ✅ Dataset Sınıfı
class IntentDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, label2id):
        self.encodings = tokenizer(texts, truncation=True, padding=True)
        self.labels = [label2id[label] for label in labels]

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item["labels"] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

# ✅ BERT Tabanlı Chatbot Sınıfı
class BERTChatbot:
    def __init__(self, device=None, response_path=None):
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
        self.label2id = {}
        self.id2label = {}
        self.model = None
        self.responses = {}  # intent -> [cevap1, cevap2, ...]
        if response_path:
            self.load_responses(response_path)

    def load_responses(self, path):
        df = pd.read_excel(path)
        for _, row in df.iterrows():
            intent = row["Intent"]
            cevaplar = [str(row[col]) for col in df.columns if col != "Intent" and pd.notna(row[col])]
            self.responses[intent] = cevaplar

    # train fonksiyonu validasyon seti alacak şekilde güncellendi
    def train(self, train_df, val_df=None):
        labels = sorted(train_df["Intent"].unique())
        self.label2id = {label: idx for idx, label in enumerate(labels)}
        self.id2label = {idx: label for label, idx in self.label2id.items()}

        train_texts = train_df["Example"].tolist()
        train_labels = train_df["Intent"].tolist()
        train_dataset = IntentDataset(train_texts, train_labels, self.tokenizer, self.label2id)

        if val_df is not None:
            val_texts = val_df["Example"].tolist()
            val_labels = val_df["Intent"].tolist()
            val_dataset = IntentDataset(val_texts, val_labels, self.tokenizer, self.label2id)
        else:
            val_dataset = None

        self.model = BertForSequenceClassification.from_pretrained(
            "bert-base-uncased",
            num_labels=len(self.label2id),
            id2label=self.id2label,
            label2id=self.label2id
        )
        self.model.to(self.device)

        training_args = TrainingArguments(
            output_dir="./bert_output",
            num_train_epochs=50,              # 50 epoch
            per_device_train_batch_size=16,
            learning_rate=2e-5,
            logging_dir="./logs",
            logging_steps=10,
            eval_strategy="epoch",     # Her epoch'ta validasyon yap
            save_strategy="epoch",           # Modeli her epoch sonunda kaydet
            load_best_model_at_end=True,     # En iyi modeli yükle
            metric_for_best_model="eval_loss",
            greater_is_better=False,
            report_to="none"
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            callbacks=[EarlyStoppingCallback(early_stopping_patience=5)]  # 3 epoch sabır
        )

        trainer.train()

    def predict_intent(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        self.model.eval()
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class_id = torch.argmax(logits).item()
            return self.id2label[predicted_class_id]

    def predict_and_respond(self, user_input):
        predicted_intent = self.predict_intent(user_input)
        cevaplar = self.responses.get(predicted_intent, ["Üzgünüm, bu konuda sana yardımcı olamıyorum."])
        return random.choice(cevaplar)

# ✅ Eğitim ve Test Dosyalarını Yükle
train_df = pd.read_excel("train.xlsx")
test_df = pd.read_excel("test.xlsx")
response_path = "intent_cevaplari.xlsx"

# ✅ Eğitim ve validasyon için train verisini böl
train_data, val_data = train_test_split(train_df, test_size=0.2, random_state=42, stratify=train_df["Intent"])

# ✅ Modeli Eğit ve Yanıt Sistemini Yükle
bot = BERTChatbot(response_path=response_path)
bot.train(train_data, val_df=val_data)

# ✅ Modeli ve etiketleri kaydet
bot.model.save_pretrained("./bert_output")
joblib.dump(bot.label2id, "label2id.pkl")

# ✅ Test: Tahmin ve Raporlama
X_test = test_df["Example"].tolist()
y_test = test_df["Intent"].tolist()
y_pred = [bot.predict_intent(text) for text in X_test]

print("\n📋 Classification Report:")
print(classification_report(y_test, y_pred))

precision = precision_score(y_test, y_pred, average="macro")
recall = recall_score(y_test, y_pred, average="macro")
f1 = f1_score(y_test, y_pred, average="macro")
print(f"\n🎯 Precision: {precision:.4f}")
print(f"🔁 Recall:    {recall:.4f}")
print(f"📏 F1 Score:  {f1:.4f}")

# ✅ Confusion Matrix
def plot_confusion_matrix(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred, labels=sorted(set(y_true)))
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=sorted(set(y_true)), yticklabels=sorted(set(y_true)))
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("📊 Confusion Matrix")
    plt.show()

plot_confusion_matrix(y_test, y_pred)

# ✅ Kullanıcıyla Etkileşim
while True:
    user_input = input("\n👤 Kullanıcı: ")
    if user_input.lower() in ["exit", "quit", "çık", "çıkış"]:
        print("👋 Görüşmek üzere!")
        break
    cevap = bot.predict_and_respond(user_input)
    print("🤖 Bot:", cevap)


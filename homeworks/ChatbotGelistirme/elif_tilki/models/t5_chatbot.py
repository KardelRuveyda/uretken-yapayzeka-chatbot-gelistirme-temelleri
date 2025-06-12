# Gerekli Kütüphaneler
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import T5Tokenizer, T5ForConditionalGeneration
from torch.optim import AdamW
from sklearn.metrics import classification_report, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import random
import numpy as np
from sklearn.model_selection import train_test_split

# Sabitler
MODEL_NAME = "google/flan-t5-base"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
MAX_INPUT_LENGTH = 128
MAX_LABEL_LENGTH = 16
BATCH_SIZE = 16
EPOCHS = 50
LEARNING_RATE = 2e-5
PATIENCE = 5

# Dataset Sınıfı
class T5IntentDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_input_len=MAX_INPUT_LENGTH, max_label_len=MAX_LABEL_LENGTH):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_input_len = max_input_len
        self.max_label_len = max_label_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        input_text = "classify intent: " + self.texts[idx]
        inputs = self.tokenizer(input_text, max_length=self.max_input_len, padding="max_length", truncation=True, return_tensors="pt")
        labels = self.tokenizer(self.labels[idx], max_length=self.max_label_len, padding="max_length", truncation=True, return_tensors="pt")

        input_ids = inputs.input_ids.squeeze()
        attention_mask = inputs.attention_mask.squeeze()
        labels_ids = labels.input_ids.squeeze()
        labels_ids[labels_ids == self.tokenizer.pad_token_id] = -100

        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask,
            "labels": labels_ids,
        }

# T5 Chatbot Sınıfı
class T5Chatbot:
    def __init__(self, model_name=MODEL_NAME, device=DEVICE, response_path=None):
        self.device = device
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)
        self.responses = {}
        if response_path:
            self.load_responses(response_path)

    def load_responses(self, path):
        df = pd.read_excel(path)
        for _, row in df.iterrows():
            intent = row["Intent"]
            cevaplar = [str(row[col]) for col in df.columns if col != "Intent" and pd.notna(row[col])]
            self.responses[intent] = cevaplar

    def train(self, df, val_df=None, epochs=EPOCHS, batch_size=BATCH_SIZE, lr=LEARNING_RATE, patience=PATIENCE):
        train_dataset = T5IntentDataset(df["Example"].tolist(), df["Intent"].tolist(), self.tokenizer)
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

        if val_df is not None:
            val_dataset = T5IntentDataset(val_df["Example"].tolist(), val_df["Intent"].tolist(), self.tokenizer)
            val_loader = DataLoader(val_dataset, batch_size=batch_size)
        else:
            val_loader = None

        optimizer = AdamW(self.model.parameters(), lr=lr)
        best_val_loss = float("inf")
        no_improve_epochs = 0
        self.model.train()

        for epoch in range(epochs):
            print(f"\nEpoch {epoch+1}/{epochs}")
            total_loss = 0

            for batch_idx, batch in enumerate(train_loader):
                input_ids = batch["input_ids"].to(self.device)
                attention_mask = batch["attention_mask"].to(self.device)
                labels = batch["labels"].to(self.device)

                outputs = self.model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss
                loss.backward()

                optimizer.step()
                optimizer.zero_grad()
                total_loss += loss.item()

                if (batch_idx + 1) % 10 == 0:
                    avg_loss = total_loss / 10
                    print(f"Batch {batch_idx+1} - Loss: {avg_loss:.4f}")
                    total_loss = 0

            # Erken durdurma kontrolü
            if val_loader:
                self.model.eval()
                val_loss = 0
                with torch.no_grad():
                    for batch in val_loader:
                        input_ids = batch["input_ids"].to(self.device)
                        attention_mask = batch["attention_mask"].to(self.device)
                        labels = batch["labels"].to(self.device)
                        outputs = self.model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
                        val_loss += outputs.loss.item()

                avg_val_loss = val_loss / len(val_loader)
                print(f"Validation Loss: {avg_val_loss:.4f}")

                if avg_val_loss < best_val_loss:
                    best_val_loss = avg_val_loss
                    no_improve_epochs = 0
                    self.save_model("./best_t5_model")
                else:
                    no_improve_epochs += 1
                    print(f"No improvement for {no_improve_epochs} epoch(s)")
                    if no_improve_epochs >= patience:
                        print("⛔ Early stopping triggered.")
                        break
                self.model.train()

    def predict_intent(self, user_input):
        self.model.eval()
        input_text = "classify intent: " + user_input
        inputs = self.tokenizer(input_text, return_tensors="pt", truncation=True, padding=True, max_length=MAX_INPUT_LENGTH).to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=MAX_LABEL_LENGTH, num_beams=4, early_stopping=True)
        intent = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return intent

    def predict_and_respond(self, user_input):
        intent = self.predict_intent(user_input)
        cevaplar = self.responses.get(intent, ["Üzgünüm, bu konuda sana yardımcı olamıyorum."])
        return random.choice(cevaplar)

    def save_model(self, path="./t5_intent_model"):
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)

    def load_model(self, path="./t5_intent_model"):
        self.tokenizer = T5Tokenizer.from_pretrained(path)
        self.model = T5ForConditionalGeneration.from_pretrained(path).to(self.device)

# Confusion Matrix Görselleştirme
def plot_confusion_matrix(y_true, y_pred, labels):
    cm = confusion_matrix(y_true, y_pred, labels=labels)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt="d", xticklabels=labels, yticklabels=labels, cmap="Blues")
    plt.xlabel("Tahmin")
    plt.ylabel("Gerçek")
    plt.title("📊 Confusion Matrix")
    plt.show()

# Ana Kod
if __name__ == "__main__":
    train_path = "train.xlsx"
    test_path = "test.xlsx"
    response_path = "intent_cevaplari.xlsx"

    train_df = pd.read_excel(train_path)
    test_df = pd.read_excel(test_path)

    # Eğitim ve validation verisini ayır
    train_df, val_df = train_test_split(train_df, test_size=0.2, stratify=train_df["Intent"], random_state=42)

    # Model oluştur
    bot = T5Chatbot(response_path=response_path)

    # Eğit
    bot.train(train_df, val_df=val_df, epochs=EPOCHS, patience=PATIENCE)

    # En iyi modeli yükle
    bot.load_model("./best_t5_model")

    # Test et
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

    # Confusion Matrix
    unique_labels = sorted(set(y_test))
    plot_confusion_matrix(y_test, y_pred, unique_labels)

    # Sohbet
    print("\n--- Chatbot ile Sohbete Başla (exit ile çık) ---")
    while True:
        user_input = input("\n👤 Kullanıcı: ")
        if user_input.lower() in ["exit", "quit", "çık", "çıkış"]:
            print("👋 Görüşmek üzere!")
            break
        cevap = bot.predict_and_respond(user_input)
        print("🤖 Bot:", cevap)


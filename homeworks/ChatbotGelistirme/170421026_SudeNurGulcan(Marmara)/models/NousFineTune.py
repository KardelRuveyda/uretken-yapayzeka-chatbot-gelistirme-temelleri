import os
import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset, DatasetDict
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
    pipeline,
    BitsAndBytesConfig
)
from peft import get_peft_model, LoraConfig, TaskType  # 🆕 LoRA

# 📂 1. Veri Setini Yükle
df = pd.read_csv("D:/Chatbot/yeniIntents.csv")
df = df[["text", "response"]].dropna()

# 🎲 2. Eğitim/Test Ayrımı (%80 - %20)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# 🤖 3. Hugging Face Dataset Formatına Dönüştür
dataset = DatasetDict({
    "train": Dataset.from_pandas(train_df.reset_index(drop=True)),
    "test": Dataset.from_pandas(test_df.reset_index(drop=True)),
})

# 🔤 4. Tokenizer ve Modeli Yükle
model_name = "NousResearch/Nous-Hermes-2-Mistral-7B-DPO"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
tokenizer.pad_token = tokenizer.eos_token

# ✂️ 5. Tokenization Fonksiyonu
def tokenize(batch):
    prompts = [f"### Soru:\n{text}\n\n### Cevap:\n{response}" for text, response in zip(batch["text"], batch["response"])]
    return tokenizer(prompts, truncation=True, padding="max_length", max_length=512)

tokenized_datasets = dataset.map(tokenize, batched=True)

# ⚙️ 6. Quantized Model Ayarları
bnb_config = BitsAndBytesConfig(load_in_8bit=True)

base_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
    quantization_config=bnb_config,
    device_map="auto"
)

# 🧩 7. LoRA (PEFT) ile Fine-Tuning yapılabilir hale getir
peft_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],  # Mistral modeline göre
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)

model = get_peft_model(base_model, peft_config)

# 🧪 8. Data Collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# ⚙️ 9. Eğitim Ayarları
training_args = TrainingArguments(
    output_dir="./finetuned_mistral",
    save_strategy="epoch",
    save_total_limit=1,
    learning_rate=2e-5,
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    logging_dir="./logs",
    report_to="none",
    fp16=torch.cuda.is_available(),
)

# 🏋️ 10. Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# 🚀 11. Eğitimi Başlat
trainer.train()

# 💾 12. Modeli ve Tokenizer'ı Kaydet
model.save_pretrained("finetuned_model")
tokenizer.save_pretrained("finetuned_model")

print("✅ Fine-tuning tamamlandı ve model kaydedildi.")

# 🧪 13. Test için Modeli Yükle
model = AutoModelForCausalLM.from_pretrained("finetuned_model")
tokenizer = AutoTokenizer.from_pretrained("finetuned_model")

gen = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

print("\n🧪 TEST SONUÇLARI:\n")

for i in range(5):
    soru = test_df.iloc[i]["text"]
    gercek_cevap = test_df.iloc[i]["response"]
    girdi = f"### Soru:\n{soru}\n\n### Cevap:"
    tahmin = gen(girdi, max_new_tokens=100)[0]["generated_text"].split("### Cevap:")[-1].strip()

    print(f"🟡 Soru: {soru}")
    print(f"✅ Gerçek Cevap: {gercek_cevap}")
    print(f"🤖 Model Tahmini: {tahmin}")
    print("—" * 50)



import os
import torch
import pandas as pd
from sklearn.model_selection import train_test_split
from datasets import Dataset, DatasetDict
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    pipeline,
    BitsAndBytesConfig
)
from peft import get_peft_model, LoraConfig, TaskType  # 🆕 LoRA
from tqdm import tqdm
from evaluate import load  # 🆕 Metrik hesaplamaları içi

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

# Modeli ve tokenizer'ı yükle
bnb_config = BitsAndBytesConfig(load_in_8bit=True)

model = AutoModelForCausalLM.from_pretrained(
    "finetuned_model",
    device_map="auto",
    quantization_config=bnb_config,
)

tokenizer = AutoTokenizer.from_pretrained("finetuned_model")

# Metin üretme pipeline'ı
gen = pipeline("text-generation", model=model, tokenizer=tokenizer, device_map="auto")

# Metrikleri yükle
rouge = load("rouge")
bertscore = load("bertscore")
bleu = load("bleu")

generated_responses = []
reference_responses = []

# Tüm test seti üzerinde tahminler
for i in tqdm(range(len(test_df))):
    soru = test_df.iloc[i]["text"]
    gercek_cevap = test_df.iloc[i]["response"]
    girdi = f"### Soru:\n{soru}\n\n### Cevap:"
    
    try:
        tahmin = gen(girdi, max_new_tokens=100)[0]["generated_text"].split("### Cevap:")[-1].strip()
    except:
        tahmin = ""

    generated_responses.append(tahmin)
    reference_responses.append(gercek_cevap)

# ROUGE hesapla
rouge_result = rouge.compute(predictions=generated_responses, references=reference_responses)

# BERTScore hesapla
bertscore_result = bertscore.compute(predictions=generated_responses, references=reference_responses, lang="en")

# BLEU hesapla (sadece ilk cümleyi baz alır)
bleu_result = bleu.compute(predictions=generated_responses, references=[[ref] for ref in reference_responses])

# Sonuçları yazdır
print("\n📊 METRİK SONUÇLARI:\n")
print("🔹 ROUGE:", rouge_result)
print("🔹 BERTScore (Precision, Recall, F1):", {
    "precision": sum(bertscore_result["precision"]) / len(bertscore_result["precision"]),
    "recall": sum(bertscore_result["recall"]) / len(bertscore_result["recall"]),
    "f1": sum(bertscore_result["f1"]) / len(bertscore_result["f1"]),
})
print("🔹 BLEU:", bleu_result)

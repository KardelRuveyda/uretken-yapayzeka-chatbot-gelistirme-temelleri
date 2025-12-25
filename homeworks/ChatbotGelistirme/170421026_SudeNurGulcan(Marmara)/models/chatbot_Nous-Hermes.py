
import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

# CSV'den intent verisini yükle
df = pd.read_csv(r"D:\Chatbot\yeniIntents.csv")

# Embedding modeli
embed_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
doc_embeddings = embed_model.encode(df["text"].tolist(), convert_to_numpy=True)

# FAISS index oluştur ve veriyi ekle
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

# FAISS index ve dökümanları kaydet
faiss.write_index(index, "faiss_index.index")
with open("docs.pkl", "wb") as f:
    pickle.dump((df["text"].tolist(), df["response"].tolist()), f)

print("✅ Embed + FAISS + Dökümanlar Hazır")

# CUDA kontrolü
if torch.cuda.is_available():
    print("🚀 CUDA destekli sistem tespit edildi (GPU kullanılacak)")
else:
    print("⚠️ GPU bulunamadı, CPU kullanılacak")

# Model adı
model_name = "NousResearch/Nous-Hermes-2-Mistral-7B-DPO"

# 4-bit quantization ayarları
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
)

# Tokenizer ve model yükle
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    quantization_config=bnb_config,
    torch_dtype=torch.float16
)
model.eval()

# RAG fonksiyonu: intent eşleşmesi + LLM cevabı
def rag_cevapla(soru, top_k=1):
    # FAISS ve dokümanları yükle
    index = faiss.read_index("faiss_index.index")
    with open("docs.pkl", "rb") as f:
        docs, responses = pickle.load(f)

    # Embed modeli (yeniden yükle)
    embed_model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    query_vec = embed_model.encode([soru], convert_to_numpy=True)

    # FAISS arama
    D, I = index.search(query_vec, top_k)

    # En yakın intent ve cevabı
    yakin_intentler = [docs[i] for i in I[0]]
    yakin_cevaplar = [responses[i] for i in I[0]]

    # Prompt oluştur
    en_yakin_bilgi = "\n".join(yakin_cevaplar)
    prompt = f"""Sen bir yemek danışmanısın. Türk ve dünya mutfağı hakkında tarif, malzeme ve pişirme yöntemlerini açıklarsın. Sorulara sade, anlaşılır ve doğru cevaplar ver.

### Soru:
{soru}

### Bilgi:
{en_yakin_bilgi}

### Cevap:"""

    # Tokenize et
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    # Modelden yanıt üret
    output = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=False,
        temperature=0.3,
        top_p=0.9,
        num_beams=4,
        early_stopping=True
    )

    cevap = tokenizer.decode(output[0], skip_special_tokens=True)
    if "### Cevap:" in cevap:
        cevap = cevap.split("### Cevap:")[-1].strip()

    # Sonuçları döndür
    return {
        "en_yakin_intent": yakin_intentler[0],
        "en_yakin_cevap": yakin_cevaplar[0],
        "model_cevabi": cevap
    }

# Örnek Soru
soru = "Merhaba"
sonuc = rag_cevapla(soru)

# Terminal çıktısı
print("👤 Soru:", soru)
print("📌 En Yakın Intent:", sonuc["en_yakin_intent"])
print("📋 Hazır Intent Cevabı:", sonuc["en_yakin_cevap"])
print("🤖 LLM Model Cevabı:", sonuc["model_cevabi"])

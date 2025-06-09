# 🌙 Dream Data Indexer – Vektör Veritabanına JSON'dan Veri Yükleme

Bu küçük Python script'i, `dream_data.json` adlı dosyadaki rüya verilerini alır ve LangChain ile Chroma vektör veritabanına dönüştürür. Ardından bu verilerden bilgi getirmek (retrieval) için kullanılabilecek bir `retriever` objesi oluşturur.

---

## 🧠 Ne İşe Yarar?

LLM tabanlı uygulamalarda, dış kaynaklardan gelen belgeleri modele **aktarılabilir** hale getirmek için önce **vektörleştirme (embedding)** yapılması gerekir.

Bu dosya:

1. Rüya verilerini `.json` formatından okur.
2. LangChain'in `Document` formatına çevirir.
3. OpenAI Embedding modeli ile vektör haline getirir.
4. Chroma vektör veritabanına ekler.
5. Sorgu yapmaya hazır bir **retriever** nesnesi oluşturur.

---

## 🔧 Gereksinimler

```bash
pip install langchain-openai langchain-core langchain-community chromadb python-dotenv
```

Ayrıca `.env` dosyanızda OpenAI API anahtarınızı tanımlayın:

```
OPENAI_API_KEY=your_api_key_here
```

---

## 🗂️ Kullanılan Dosyalar

### 📄 `dream_data.json`

Örnek veri yapısı şöyle olmalıdır:

```json
{
  "dreams": [
    {
      "page_content": "Rüyamda gökyüzünde uçuyordum.",
      "metadata": {
        "source": "rüya_defteri",
        "date": "2025-06-10"
      }
    },
    ...
  ]
}
```

---

## 🧾 Kodun Açıklaması

```python
import json
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
```

- Gerekli modüller yükleniyor.
- `.env` dosyasındaki API anahtarları okunuyor.

```python
load_dotenv()
path = "..."  # dream_data.json dosyasının yolu
```

- Dosya yolu belirtilir, JSON dosyası açılır ve içerik `dream_data` olarak okunur.

```python
with open(path, "r", encoding="utf-8") as file:
    dream_data = json.load(file)
```

- JSON formatındaki `dreams` listesi `Document` objelerine dönüştürülür.

```python
documents = [
    Document(
        page_content=dream["page_content"],
        metadata=dream["metadata"]
    )
    for dream in dream_data["dreams"]
]
```

- Belgeler OpenAI'ın embedding modeli ile vektörleştirilir ve Chroma'ya kaydedilir.

```python
vectorstore = Chroma.from_documents(
    documents=documents,
    collection_name="dream-chroma",
    embedding=OpenAIEmbeddings(),
    persist_directory="./.chroma_dreams"
)
```

- Artık bu vektör verisi üzerinden bilgi çağırmak mümkündür. Aşağıdaki retriever nesnesi bunun için kullanılır:

```python
retriever = vectorstore.as_retriever()
```

---

## 📌 Sonuç

Bu betik, LLM tabanlı bir bilgi getirme (retrieval) uygulamasına ilk veri yüklemesini yapar. Özellikle RAG (Retrieval-Augmented Generation) yapılarında temel adımdır.

---

## ▶️ Çalıştırmak için

```bash
python ingest_dreams.py
```

(`ingest_dreams.py` sizin script dosyanızın adı olmalıdır.)

---
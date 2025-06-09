# 🌌 LangGraphProject – Advanced RAG + Self-Reflection

Bu proje, **Retrieval-Augmented Generation (RAG)** mimarisinin gelişmiş bir uygulamasıdır. LangGraph altyapısı ile sorgulara doğru, kaynaklı ve değerlendirilebilir cevaplar üretmek hedeflenmiştir.

---

## 📁 Proje Yapısı

```bash
LangGraphProject/
├── data/
│   └── dream_data.json           # Örnek belge veri seti
├── graph/
│   ├── chains/                   # Chain'ler (zincirler)
│   │   ├── answer_grader.py
│   │   ├── generation.py
│   │   ├── hallucination_grader.py
│   │   ├── retrieval_grader.py
│   │   └── router.py
│   ├── nodes/                    # Node'lar (düğümler)
│   │   ├── generate.py
│   │   ├── retrieve.py
│   │   ├── grade_documents.py
│   │   ├── web_search.py
│   │   └── node_constants.py
│   ├── graph.py                  # LangGraph DAG tanımı
│   ├── state.py                  # State yapısı
│   └── __init__.py
├── ingestion.py                 # Belgeleri vektör veritabanına yükler
├── main.py                      # Uygulama başlangıç noktası
├── .env                         # Ortam değişkenleri
└── requirements.txt             # Bağımlılıklar
```

---

## 🔍 Nedir Bu Proje?

LangChain ve LangGraph tabanlı bu sistem:

- 🧠 LLM ile metin üretir.
- 🔍 Sorguya en uygun belgeleri getirir.
- ✅ Yanıtların doğruluğunu ve güvenilirliğini değerlendirir.

---

## 🔄 Chain’ler (Zincirler)

### `graph/chains/`

Zincirler, bir işlemin adımlarını tanımlar:

- **generation.py** → Sorguyu alır, belgeleri getirir, model ile yanıt üretir.
- **answer_grader.py** → Model yanıtını değerlendirir.
- **retrieval_grader.py** → Geri getirilen belgelerin kalitesini puanlar.
- **hallucination_grader.py** → Halüsinasyon içerip içermediğini ölçer.
- **router.py** → Sorguya uygun zinciri seçer.

---

## ⚙️ Node’lar (Düğümler)

### `graph/nodes/`

Her node tekil bir işi yapar. Chain’lerde birleştirilerek akış oluşturulur.

- **generate.py** → LLM ile cevap üretir.
- **retrieve.py** → Chroma’dan belge getirir.
- **grade_documents.py** → Belge-soru ilgisini değerlendirir.
- **web_search.py** → Harici web araması (isteğe bağlı).
- **node_constants.py** → Sabitler.
- **state.py** → Sorgu, belgeler, yanıtlar ve puanlamaları taşır.

---

## 🧠 graph.py – Akışın Beyni

LangGraph ile DAG (Directed Acyclic Graph) yapısı kurulur. Hangi adımın ne zaman çalışacağı belirlenir.

---

## 💾 ingestion.py – Veri İndeksleme

`dream_data.json` dosyasındaki belgeleri ChromaDB’ye yükler. Bu sayede belge araması yapılabilir.

```bash
$ python ingestion.py
```

---

## ▶️ main.py – Uygulamayı Başlat

Tüm sistemi test etmek veya komut satırından çalıştırmak için:

```bash
$ python main.py
```

---

## ✅ Örnek Akış

1. Kullanıcı: `"Rüyamda uçuyordum bu ne demek?"`
2. `router.py`: Sorgunun tipi belirlenir.
3. `retrieve.py`: İlgili belgeler ChromaDB’den çekilir.
4. `generate.py`: Model yanıt üretir.
5. `answer_grader.py`: Yanıt değerlendirir.
6. `hallucination_grader.py`: Gerçeklik kontrolü yapılır.
7. `state.py`: Tüm bilgiler toparlanır ve yanıt döner.

---

## 🧩 Teknolojiler

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [LangChain](https://www.langchain.com/)
- [ChromaDB](https://www.trychroma.com/)
- [OpenAI API](https://platform.openai.com/)
- Python 3.10+

---

## 📌 Kurulum

```bash
git clone https://github.com/kullaniciadi/LangGraphProject.git
cd LangGraphProject
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

`.env` dosyasını doldurun:

```
OPENAI_API_KEY=...
CHROMA_DB_PATH=...
```

## 🪄 Not

Bu yapı, LangGraph üzerinde gerçek bir agent mimarisinin nasıl kurulabileceğini öğrenmek için harika bir örnektir. Özellikle **self-reflection**, **query grading**, **halüsinasyon kontrolü** gibi ileri seviye konular dahil edilmiştir.

---
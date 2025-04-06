
# ChatOpenAI ile Temel LangChain RAG Kullanımı


## 🔧 Gerekli Kurulumlar

```bash
pip install langchain
pip install langchain-openai
pip install python-dotenv
```

`.env` dosyasına aşağıdaki şekilde OpenAI API anahtarınızı ekleyin:

```
OPENAI_API_KEY=your-api-key
```

---

## 🔍 Embedding: OpenAIEmbeddings Kullanımı

```python
from langchain.embeddings import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

### Açıklama:

- `OpenAIEmbeddings`: Metinleri sayısal vektörlere dönüştürmek için kullanılır.
- `text-embedding-3-large`: OpenAI'nin en güncel embedding modellerinden biridir. Daha büyük bağlamlar için daha iyi semantik temsil sağlar.
- Bu vektörler, metinlerin anlamını sayısal olarak temsil eder ve benzerlik karşılaştırmaları için kullanılır.

---

## 🤖 Chat: GPT-4o Modeli ile Sohbet

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    max_tokens=500
)
```

### Açıklama:

- `ChatOpenAI`: LangChain arayüzü ile OpenAI'nin LLM'lerini kullanmak için yapılandırılmış sınıftır.
- `gpt-4o`: OpenAI'nin en yeni ve gelişmiş çok modlu modelidir.
- `temperature=0.3`: Cevapların daha kararlı ve tutarlı olması için düşük rastgelelik sağlar.
- `max_tokens=500`: Maksimum yanıt uzunluğunu belirler.

---

## 📌 Örnek Kullanım

```python
response = llm.invoke("LangChain nedir?")
print(response)
```

Bu komut, GPT-4o modelinden `LangChain` hakkında açıklayıcı bir cevap döndürmesini sağlar.

---

## 📎 Ek Bilgiler

- LangChain hakkında daha fazla bilgi için: [https://docs.langchain.com](https://docs.langchain.com)
- OpenAI API belgeleri: [https://platform.openai.com/docs](https://platform.openai.com/docs)

---

## 🔗 Kaynak Notebook

Notebook dosyasına erişmek için:  
📂 [openai_basic_rag.ipynb](https://github.com/KardelRuveyda/uretken-yapayzeka-chatbot-gelistirme-temelleri/blob/master/examples/02_openai_chatbot/openai_basic_rag.ipynb)

📖 Detaylı anlatım, kod blokları, ekran çıktıları ve görsel açıklamalar için lütfen orijinal makaleyi okuyun. Gemini ile aynı işlemleri yaptık sadece LLM değişti. O nedenle diğer aşamalar için tekrardan bu makaleyi inceleyebilirsiniz.
👉 <a href="https://ruveydakardelcetin.medium.com/gemini-ve-langchain-kullanarak-rag-ile-chatbot-geli%C5%9Ftirme-c6b6b03ad854" target="_blank">Gemini ve LangChain Kullanarak RAG ile Chatbot Geliştirme</a>

🎬 Video anlatımı için:  
👉 <a href="https://www.youtube.com/live/oWlaMUcOWYM?si=N5iuEmLDseY9g_yO" target="_blank">YouTube: Gemini ve LangChain ile RAG Uygulaması</a>
---



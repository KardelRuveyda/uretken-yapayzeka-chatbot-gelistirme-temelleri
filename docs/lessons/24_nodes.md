# 🎓 `nodes/` Klasörü – Ne İşe Yarar ?

Bu doküman, `nodes/` klasöründe bulunan her `.py` dosyasının **ne işe yaradığını** ve **satır satır nasıl çalıştığını** detaylı şekilde açıklar. Eğitim amaçlı hazırlanmıştır ve öğrencilere bu yapı taşlarını öğretmeyi hedefler.

---

## 🧠 `generate.py` – Modelden Cevap Üretme

### Bu dosya ne yapar?

- Kullanıcının sorusu ve sistemin bulduğu belgeleri alır.
- Bu bilgilerle LLM modelini çalıştırır.
- LLM'in ürettiği yanıtı döndürür.

### Kod ve Açıklama

```python
from typing import Any, Dict  # Fonksiyonun giriş-çıkış türlerini belirtir
from graph.chains.generation import generation_chain  # Daha önce tanımlanmış olan yanıt üretme zinciri
from graph.state import GraphState  # Verinin akışını tutan yapıdır
```

```python
def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE---")  # Takip için log basılır
```

```python
    question = state["question"]  # Kullanıcı sorusunu al
    documents = state["documents"]  # İlgili belgeleri al
```

```python
    generation = generation_chain.invoke({  # Zinciri çalıştır, model yanıt üretsin
        "context": documents,
        "question": question
    })
```

```python
    return {
        "documents": documents,  # Belgeleri koru
        "question": question,    # Soruyu koru
        "generation": generation # Üretilen cevabı döndür
    }
```

---

## 📚 `retrieve.py` – Belgeleri Getirme

### Bu dosya ne yapar?

- Kullanıcının sorusuna uygun belgeleri vektör veritabanından getirir.
- Bu belgeler, sonraki adımda modele bağlam sağlamak için kullanılır.

### Kod ve Açıklama

```python
from typing import Any, Dict
from graph.state import GraphState
from ingestion import retriever  # ChromaDB'den belge çeken yapı
```

```python
def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")  # Debug mesajı
```

```python
    question = state["question"]  # Kullanıcı sorusunu al
    documents = retriever.invoke(question)  # Soruya uygun belgeleri al
```

```python
    return {
        "documents": documents,  # Belgelerle yeni state dön
        "question": question
    }
```

---

## 🧪 `grade_documents.py` – Belgelerin Alakalılığını Değerlendirme

### Bu dosya ne yapar?

- Getirilen belgelerin gerçekten kullanıcı sorusuyla ilgili olup olmadığını kontrol eder.
- Alakalı olmayanları filtreler.
- Eğer yeterince belge yoksa sistemin web araması yapmasına karar verir.

### Kod ve Açıklama

```python
from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState
from typing import Any, Dict
```

```python
def grade_documents(state: GraphState) -> Dict[str, Any]:
    """ Belgelerin soruyla ilgili olup olmadığını değerlendirir """
    print("---CHECK DOCUMENT RELEVANCE TO QUESTION")
```

```python
    question = state["question"]
    documents = state["documents"]
    filtered_docs = []  # Alakalı belgeler burada toplanır
    web_search = False  # Belge yetersizse True yapılır
```

```python
    for d in documents:
        score = retrieval_grader.invoke({
            "question": question,
            "document": d.page_content
        })
        grade = score.binary_score  # "yes" ya da "no"
```

```python
        if grade.lower() == "yes":
            print("---GRADE : DOCUMENT RELEVANT---")
            filtered_docs.append(d)
        else:
            print("---GRADE : DOCUMENT NOT RELEVANT")
            web_search = True
```

```python
    return {
        "documents": filtered_docs,
        "question": question,
        "web_search": web_search
    }
```

---

## 🌐 `web_search.py` – Web Tabanlı Bilgi Arama

### Bu dosya ne yapar?

- Eğer yerel belgeler yetersizse, dış kaynaktan bilgi çeker.
- Tavily API ile internette arama yapar.
- Sonuçları yeni belge olarak mevcutlara ekler.

### Kod ve Açıklama

```python
from typing import Any, Dict
from langchain.schema import Document
from langchain_community.tools.tavily_search import TavilySearchResults
from graph.state import GraphState

web_search_tool = TavilySearchResults()  # Aracı oluştur
```

```python
def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
```

```python
    question = state["question"]
    documents = state["documents"]
```

```python
    docs = web_search_tool.invoke({"query": question})  # Web araması yap
    web_results = "\n".join([d["content"] for d in docs])  # Sonuçları birleştir
    web_results = Document(page_content=web_results)  # Tek belge haline getir
```

```python
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
```

```python
    return {
        "documents": documents,
        "question": question
    }
```

---

## 📦 `__init__.py` – Klasörü Modül Haline Getirme

### Bu dosya ne yapar?

- `nodes` klasörünün dışarıdan Python modülü gibi çağrılmasını sağlar.
- Hangi fonksiyonların dışarıdan erişilebileceğini belirtir.

```python
from graph.nodes.generate import generate
from graph.nodes.grade_documents import grade_documents
from graph.nodes.retrieve import retrieve
from graph.nodes.web_search import web_search

__all__ = ["generate", "grade_documents", "retrieve", "web_search"]
```

---


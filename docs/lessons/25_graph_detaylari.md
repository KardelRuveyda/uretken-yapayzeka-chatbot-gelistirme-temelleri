
# 🔍 Derinlemesine İnceleme: `graph.py`, `state.py`, `node_constants.py`

Bu döküman, LangGraph mimarisi kullanan bir yapay zeka projesinde temel akışı kontrol eden 3 önemli dosyayı **satır satır** ve **yorumlarla** açıklar. Bu açıklamalar, konuya yabancı biri için bile anlaşılabilir olacak şekilde yapılandırılmıştır.

---

## 1️⃣ `state.py` – Sistemdeki Verinin Tanımı

```python
from typing import List, TypedDict
```

* Bu satır, Python'un type hinting (tip belirleme) sisteminden iki yapı içe aktarır:

  * `List`: Bir liste tipinde değişkeni tanımlamak için.
  * `TypedDict`: Sözlük gibi çalışan ama her alanı önceden belirlenmiş, tipli veri yapısı oluşturur.

```python
class GraphState(TypedDict):
    """
    Represents the state of your graph.

    Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
    """
```

* `GraphState` sınıfı sistemin her adımda taşıdığı durumu (state) ifade eder.
* LangGraph içinde bu yapı, her node'a (düğüm) giren ve çıkan veriyi belirler.

```python
    question: str
    generation: str
    web_search: bool
    documents: List[str]
```

* `question`: Kullanıcının sorduğu metin.
* `generation`: Modelin oluşturduğu cevaptır.
* `web_search`: Eğer belgeler yetersizse, dış kaynaklardan (web) bilgi çekilecek mi?
* `documents`: Vektör veritabanından veya web'den dönen belgeler.

---

## 2️⃣ `node_constants.py` – Düğümlerin Sabit Adları

```python
RETRIEVE = "retrieve"
GRADE_DOCUMENTS = "grade_documents"
GENERATE = "generate"
WEBSEARCH = "websearch"
```

* Her bir sabit, LangGraph akışında kullanılan bir **düğümün ismini** temsil eder.
* Bu yaklaşım "magic string" hatalarını önler, kodu daha okunabilir ve hatasız hale getirir.

---

## 3️⃣ `graph.py` – Tüm Akışın Tanımlandığı Ana Yapı

### 📥 Gerekli Modüller

```python
from dotenv import load_dotenv
from langgraph.graph import StateGraph, END
```

* `.env` dosyasındaki OpenAI veya Tavily API anahtarları gibi bilgileri yükler.
* `StateGraph`: LangGraph yapısının temel sınıfı.
* `END`: Akışın bitiş noktası.

### 🔗 Diğer Dosyalardan Gelen Bileşenler

```python
from graph.chains.answer_grader import answer_grader
from graph.chains.hallucination_grader import hallucination_grader
from graph.chains.router import question_router, RouteQuery
from graph.node_constants import RETRIEVE, GRADE_DOCUMENTS, GENERATE, WEBSEARCH
from graph.nodes import generate, grade_documents, retrieve, web_search
from graph.state import GraphState
```

* Bu satırlar, zincirleri (chains), düğümleri (nodes), sabit isimleri (constants) ve `GraphState` yapısını içe aktarır.

### 🌐 Ortam Değişkenlerini Yükle

```python
load_dotenv()
```

* .env dosyasındaki API anahtarlarını otomatik olarak belleğe alır.

---

### ⚖️ Karar Fonksiyonları

#### `decide_to_generate`

```python
def decide_to_generate(state):
    print("---ASSESS GRADED DOCUMENTS---")
    if state["web_search"]:
        print("---DECISION: INCLUDE WEB SEARCH---")
        return WEBSEARCH
    else:
        print("---DECISION: GENERATE---")
        return GENERATE
```

* Belgeler yeterli değilse web araması tetiklenir.
* `web_search == True` ise -> `WEBSEARCH`, değilse -> `GENERATE`

#### `grade_generation_grounded_in_documents_and_question`

```python
def grade_generation_grounded_in_documents_and_question(state: GraphState) -> str:
    print("---CHECK HALLUCINATIONS---")
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]

    score = hallucination_grader.invoke({"documents": documents, "generation": generation})
```

* İlk olarak cevap "belgelere dayalı mı" kontrol edilir.

```python
    if hallucination_grade := score.binary_score:
        print("---GENERATION IS GROUNDED---")
        score = answer_grader.invoke({"question": question, "generation": generation})
```

* Eğer cevabın kaynaklarla uyumlu olduğu belirlenirse, ardından soruya gerçekten yanıt verip vermediği kontrol edilir.

```python
        if answer_grade := score.binary_score:
            return "useful"
        else:
            return "not useful"
    else:
        return "not supported"
```

* Halüsinasyon yok ve soru yanıtlandıysa `useful`,
* Halüsinasyon yok ama soru cevaplanmadıysa `not useful`,
* Halüsinasyon varsa `not supported`

#### `route_question`

```python
def route_question(state: GraphState) -> str:
    question = state["question"]
    source: RouteQuery = question_router.invoke({"question": question})
    if source.datasource == WEBSEARCH:
        return WEBSEARCH
    elif source.datasource == "vectorstore":
        return RETRIEVE
```

* Sorunun tipi analiz edilir ve uygun veri kaynağı seçilir.
* Örn: "rüyada Tarja Turunen görmek" → websearch

---

### 🧱 Workflow’un Tanımlanması

```python
workflow = StateGraph(GraphState)
```

* Grafik sistemimizin temel taşıdır. Her node burada tanımlanır.

#### 🔘 Node Tanımları

```python
workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)
```

* Sistemde çalışacak tüm düğümler burada belirlenir.

#### 🚪 Giriş Noktası

```python
workflow.set_conditional_entry_point(
    route_question,
    {
        WEBSEARCH: WEBSEARCH,
        RETRIEVE: RETRIEVE
    }
)
```

* Sisteme ilk giren sorgu burada yönlendirilir. Router ne karar verirse ona göre başlar.

#### 🔀 Koşullu Geçişler

```python
workflow.add_conditional_edges(GRADE_DOCUMENTS, decide_to_generate, {...})
workflow.add_conditional_edges(GENERATE, grade_generation_grounded_in_documents_and_question, {...})
```

* Belge kalitesi veya cevabın yeterliliğine göre bir sonraki düğüm seçilir.

#### 🔁 Diğer Geçişler

```python
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)
```

* Web araması yapıldıktan sonra yeniden cevap üretilir.
* Cevap başarılıysa akış sonlanır.

---

### 📦 Workflow Derlemesi ve Çıktısı

```python
app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")
```

* Akış derlenir ve Mermaid formatında grafik haline getirilip görsel olarak kaydedilir.

---

## ✅ SONUÇ

Bu üç dosya birlikte çalışarak:

* Sorgunun doğru yere yönlendirilmesini sağlar (`router`)
* Belgelerin uygunluğunu değerlendirir (`grader`)
* Yanıtın tutarlılığını ve doğruluğunu test eder (`hallucination + answer grader`)
* Ve nihayetinde cevabı üretir ya da tekrar sorgular (`generate + retry`)

Bu yapı ile güvenilir, açıklanabilir ve otomatik hatalardan kaçınan bir RAG sistemi kurmuş oluruz.

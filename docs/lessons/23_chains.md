# 🧠 `graph/chains/` Klasörü – Ne İşe Yarar? + Satır Satır Açıklama

Bu klasör, LangChain + LangGraph sisteminde zincirleri (chain) içerir. Her zincir belirli bir işi otomatikleştirir:
örneğin cevap üretme, puanlama, yönlendirme gibi. Aşağıda her dosyanın **amacı** ve **satır satır açıklaması** yer alır.

---

## 🔁 1. `generation.py` – Cevap Üreten Ana Zincir

### Ne Yapar?

- Kullanıcının sorusunu ve belgeleri modele verir.
- OpenAI LLM modeli ile cevap üretir.
- Bu cevabı sade metin olarak döner.

### Kod ve Açıklama

```python
from langchain import hub  # Hazır prompt şablonları için merkezi sistem
from langchain_core.output_parsers import StrOutputParser  # Model çıktısını düz metne çeviren yapı
from langchain_openai import ChatOpenAI  # OpenAI'nin sohbet modelini kullanmak için
```

```python
llm = ChatOpenAI(temperature=0)  # Kararlı (deterministik) cevaplar için sıcaklık 0 yapılır
prompt = hub.pull("rlm/rag-prompt")  # LangChain Hub'dan "retrieval-based QA" promptu alınır
```

```python
generation_chain = prompt | llm | StrOutputParser()  # Zincir oluşturulur: prompt → model → string çıktı
```

---

## ✅ 2. `answer_grader.py` – Cevap Doğru mu?

### Ne Yapar?

- Modelin cevabı soruyu gerçekten yanıtlıyor mu?
- LLM'e "Bu cevap soruyu açıklıyor mu?" diye sorar.
- Binary cevap döner: `yes` veya `no`.

### Kod ve Açıklama

```python
from langchain_core.prompts import ChatPromptTemplate  # LLM'e gidecek mesaj formatı
from langchain_core.pydantic_v1 import BaseModel, Field  # Yapısal veri şeması tanımlamak için
from langchain_core.runnables import RunnableSequence  # Zinciri tanımlamak için
from langchain_openai import ChatOpenAI  # OpenAI LLM
from dotenv import load_dotenv  # Ortam değişkenlerini yüklemek için
```

```python
load_dotenv()  # .env dosyasındaki anahtarları belleğe alır
class GradeAnswer(BaseModel):
    binary_score: bool = Field(
        description="Answer addresses the question 'yes' or 'no'"
    )
```

```python
llm = ChatOpenAI(temperature=0)
structured_llm_grader = llm.with_structured_output(GradeAnswer)  # Modelden yapılandırılmış çıktı bekleriz
```

```python
system = """You are a grader assessing whether an answer addresses the question.
Give a binary score 'yes' or 'no'."""

answer_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "User question: {question}\n\n LLM Generation: {generation}")
])
```

```python
answer_grader: RunnableSequence = answer_prompt | structured_llm_grader  # Zincir: prompt → model
```

---

## 📎 3. `retrieval_grader.py` – Belge Alakalı mı?

### Ne Yapar?

- Getirilen belge soruyla ilgili mi?
- LLM'e bu soruyu sorar ve `yes/no` cevabı alır.

### Kod ve Açıklama

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
```

```python
llm = ChatOpenAI(temperature=0)
class GradeDocuments(BaseModel):
    binary_score: str = Field(description="yes or no")  # Cevap: "yes" veya "no"
```

```python
structured_llm_grader = llm.with_structured_output(GradeDocuments)

system = """You are a grader assessing relevance of a document to a question.
Return 'yes' if relevant, 'no' otherwise."""
```

```python
grade_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "Document: {document}\n\nQuestion: {question}")
])

retrieval_grader = grade_prompt | structured_llm_grader  # Zincir oluşturulur
```

---

## 🚫 4. `hallucination_grader.py` – Cevap Halüsinasyon mu?

### Ne Yapar?

- Cevap, gerçekten verilen belgelerle destekleniyor mu?
- Modelin uydurma yapıp yapmadığını test eder.

### Kod ve Açıklama

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
```

```python
llm = ChatOpenAI(temperature=0)
class GradeHallucinations(BaseModel):
    binary_score: bool = Field(
        description="Answer is grounded in the facts, 'yes' or 'no'"
    )
```

```python
structured_llm_grader = llm.with_structured_output(GradeHallucinations)

system = """You are a grader assessing whether an answer is supported by given facts.
Return 'yes' or 'no'."""

hallucination_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "Facts: {documents}\n\nAnswer: {generation}")
])

hallucination_grader = hallucination_prompt | structured_llm_grader
```

---

## 🔀 5. `router.py` – Sorgu Yönlendirme

### Ne Yapar?

- Soru web'den mi cevaplanmalı yoksa veri tabanından mı?
- LLM'e yönlendirme yaptırır: `"vectorstore"` veya `"websearch"`

### Kod ve Açıklama

```python
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
```

```python
class RouteQuery(BaseModel):
    datasource: Literal["vectorstore", "websearch"] = Field(
        ..., description="Choose to route to vectorstore or websearch."
    )
```

```python
llm = ChatOpenAI(temperature=0)
structured_llm_router = llm.with_structured_output(RouteQuery)

system = """You are an expert router.
Use 'vectorstore' for symbolic dream analysis. Use 'websearch' for all else."""

route_prompt = ChatPromptTemplate.from_messages([
    ("system", system),
    ("human", "{question}")
])

question_router = route_prompt | structured_llm_router
```

---

## 📦 6. `__init__.py` – Zincirleri Paketleme

```python
from graph.chains.answer_grader import answer_grader
from graph.chains.generation import generation_chain
from graph.chains.retrieval_grader import retrieval_grader
from graph.chains.hallucination_grader import hallucination_grader
from graph.chains.router import question_router

__all__ = [
    "answer_grader",
    "generation_chain",
    "retrieval_grader",
    "hallucination_grader",
    "question_router"
]
```

> Bu dosya sayesinde zincirler dışarıdan erişilebilir hale gelir.


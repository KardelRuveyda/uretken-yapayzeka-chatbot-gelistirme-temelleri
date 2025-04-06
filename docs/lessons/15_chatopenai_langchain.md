
# ChatOpenAI ile Temel LangChain RAG Kullanımı


## 1. Gerekli Kurulumlar

```bash
pip install langchain-openai python-dotenv
```

---

## 2. OpenAI API Key Nasıl Alınır?

1. https://platform.openai.com/signup adresinden bir hesap oluştur.
2. Giriş yaptıktan sonra [API Keys](https://platform.openai.com/account/api-keys) sayfasına git.
3. **Create new secret key** butonuna tıkla ve anahtarı `.env` dosyasına şöyle ekle:

```env
OPENAI_API_KEY=sk-xxx...xxx
```

---

## 3. ChatOpenAI Sınıfının Kullanımı

```python
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)
```

- `model="gpt-3.5-turbo"`: Kullanılan LLM modeli
- `temperature=0.3`: Yanıtların tutarlılık düzeyi (0.0 → deterministik, 1.0 → yaratıcı)

---

## 4. Sorgu Gönderme

```python
response = llm.invoke("What is LangChain?")
print(response.content)
```

---

## 🔗 Kaynak Notebook

Notebook dosyasına erişmek için:  
📂 [openai_basic_rag.ipynb](https://github.com/KardelRuveyda/uretken-yapayzeka-chatbot-gelistirme-temelleri/blob/master/examples/02_openai_chatbot/openai_basic_rag.ipynb)

📖 Detaylı anlatım, kod blokları, ekran çıktıları ve görsel açıklamalar için lütfen orijinal makaleyi okuyun. Gemini ile aynı işlemleri yaptık sadece LLM değişti. O nedenle diğer aşamalar için tekrardan bu makaleyi inceleyebilirsiniz.
👉 <a href="https://ruveydakardelcetin.medium.com/gemini-ve-langchain-kullanarak-rag-ile-chatbot-geli%C5%9Ftirme-c6b6b03ad854" target="_blank">Gemini ve LangChain Kullanarak RAG ile Chatbot Geliştirme</a>

🎬 Video anlatımı için:  
👉 <a href="https://www.youtube.com/live/oWlaMUcOWYM?si=N5iuEmLDseY9g_yO" target="_blank">YouTube: Gemini ve LangChain ile RAG Uygulaması</a>
---



Bu rehberde, Hugging Face üzerinde barındırılan açık kaynak modeller ile nasıl RAG (Retrieval-Augmented Generation) tabanlı bir chatbot geliştirileceği anlatılmaktadır. Ayrıca Hugging Face API anahtarının (token) nasıl alınacağı da adım adım açıklanmıştır.

---

## 📌 Hugging Face Nedir?

[Hugging Face](https://huggingface.co), yapay zeka ve doğal dil işleme (NLP) topluluğu tarafından oluşturulan, binlerce açık kaynaklı modeli barındıran bir platformdur. LangChain gibi framework’ler Hugging Face’teki modelleri kolayca kullanmanıza imkân tanır.

---

## 📦 Kurulum

Aşağıdaki kütüphanelerin yüklü olduğundan emin olun:

```bash
pip install langchain langchain-community langchain-huggingface huggingface_hub python-dotenv
```

Proje kök dizinine `.env` dosyası ekleyin ve Hugging Face API token'ınızı içine yazın:

```
HUGGINGFACEHUB_API_TOKEN=hf_***************
```

---

## 🔐 Hugging Face API Token Nasıl Alınır?

1. Hugging Face hesabınıza giriş yapın: https://huggingface.co
2. Sağ üstten profil resminize tıklayın ve "Settings" (Ayarlar) kısmına girin.
3. Sol menüde "Access Tokens" bölümüne tıklayın.
4. “New token” butonuna tıklayın.
5. Token'a bir isim verin ve `read` yetkisiyle oluşturun.
6. Token'ı kopyalayıp `.env` dosyanıza yapıştırın.

---

## 🔡 Embedding Modeli (Vektörleştirme)

```python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
```

Bu kodda Hugging Face üzerinden `sentence-transformers/all-MiniLM-L6-v2` modeli kullanılarak embedding (vektör temsili) oluşturulmaktadır. Bu model oldukça hızlı ve küçük boyutlu olduğu için RAG senaryoları için uygundur.

---

## 🧠 LLM (Dil Modeli) Kullanımı

```python
from langchain_community.llms import HuggingFaceHub
import os

llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    model_kwargs={
        "temperature": 0.3,
        "max_new_tokens": 100
    },
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)
```

Bu örnekte `zephyr-7b-beta` adlı büyük dil modeli kullanılmaktadır. `temperature` değeri, modelin cevaplarının ne kadar yaratıcı olacağını kontrol eder. `max_new_tokens` ise modelin vereceği maksimum token (kelime parçası) sayısını sınırlar.

---

## ✅ Özet

- Hugging Face, açık kaynak modelleri ile RAG chatbot geliştirmede güçlü bir çözümdür.
- Embedding için `all-MiniLM-L6-v2` modeli hızlı ve etkili bir seçimdir.
- HuggingFaceHub ile güçlü LLM’leri API aracılığıyla kullanabilirsiniz.
- Token güvenliği için `.env` kullanmak en iyi uygulamadır.

---

## 🔗 Kaynak Notebook

Notebook dosyasına erişmek için:  
📂 [hugginface_basic_rag.ipynb](https://github.com/KardelRuveyda/uretken-yapayzeka-chatbot-gelistirme-temelleri/blob/master/examples/03_huggingface_chatbot/hugginface_basic_rag.ipynb)

📖 Detaylı anlatım, kod blokları, ekran çıktıları ve görsel açıklamalar için lütfen orijinal makaleyi okuyun. Gemini ile aynı işlemleri yaptık sadece LLM değişti. O nedenle diğer aşamalar için tekrardan bu makaleyi inceleyebilirsiniz.

👉 <a href="https://ruveydakardelcetin.medium.com/gemini-ve-langchain-kullanarak-rag-ile-chatbot-geli%C5%9Ftirme-c6b6b03ad854" target="_blank">Gemini ve LangChain Kullanarak RAG ile Chatbot Geliştirme</a>


🎬 Video anlatımı için:  
👉 <a href="https://www.youtube.com/live/oWlaMUcOWYM?si=N5iuEmLDseY9g_yO" target="_blank">YouTube: Gemini ve LangChain ile RAG Uygulaması</a>





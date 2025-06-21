### 1️⃣ Gerekli Paketlerin Kurulumu

Proje için temel bağımlılıklar aşağıdaki gibidir. Bunlar `requirements.txt` dosyasına zaten dahil edilmiştir, ancak manuel kurulum yapmak isteyenler için:

```bash
pip install beautifulsoup4==4.12.3
pip install langchain==0.2.7
pip install langgraph==0.1.8
pip install langchainhub==0.1.20
pip install langchain-community==0.2.7
pip install tavily-python==0.3.4
pip install langchain-chroma==0.1.2
pip install langchain-openai==0.1.16
pip install python-dotenv==1.0.1
pip install pytest==8.2.2
```

Alternatif olarak, tek satırda yüklemek için:

```bash
pip install -r requirements.txt
```

---

### 2️⃣ Ortam Değişkenlerini Tanımlama – `.env`

Projede API anahtarlarını, proje adlarını ve özel yapılandırmaları `.env` dosyası üzerinden yönetiyoruz.

Proje kök dizinine `.env` adında bir dosya oluşturun ve aşağıdaki değişkenleri girin:

```env
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_if_needed
LANGCHAIN_TRACING_V2=false
LANGCHAIN_PROJECT=""
PYTHONPATH=.
```

#### Açıklamalar:

- `OPENAI_API_KEY`: OpenAI erişim anahtarınız.
- `TAVILY_API_KEY`: Eğer web araması kullanıyorsanız [Tavily](https://www.tavily.com/) API key'iniz.
- `LANGCHAIN_TRACING_V2`: Takip özelliği. Geliştirme dışı genelde `false` bırakılır.
- `LANGCHAIN_PROJECT`: Proje adlandırması için isteğe bağlıdır.
- `PYTHONPATH=.`: Yerel modüllerin doğru şekilde import edilmesini sağlar.

---

### ✅ Hazır mıyız?

Yukarıdaki adımları tamamladıktan sonra artık sistemi başlatabilirsiniz:

```bash
python ingestion.py    # Belgeleri vektör veritabanına ekler
python main.py         # Sistemi başlatır ve test eder
```
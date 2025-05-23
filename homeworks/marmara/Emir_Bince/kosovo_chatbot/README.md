# 🌍 Kosovo Chatbot 🇽🇰

A conversational assistant powered by Google Gemini and a custom-trained intent classification model. It answers questions **only about the Republic of Kosovo**, greets users, says goodbye, and gracefully rejects unrelated queries.

---

## 🚀 Setup Instructions

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Gemini API key**
   Create a `.env` file in the project root and add:
   ```
   GEMINI_API_KEY=[YOUR_API_KEY_HERE]
   ```

5. **Train the intent classifier**
   ```bash
   python models/train_intent_classifier.py
   ```

6. *(Optional)* Evaluate the classifier
   ```bash
   python models/classifier_stats.py
   ```

7. **Run the chatbot**
   ```bash
   streamlit run app/streamlist_app.py
   ```

---

## 🤖 Why Gemini 2.0 Flash?

The `models/gemini-2.0-flash` model was selected for its **speed and efficiency**, providing near-instant responses at a lower computational cost. While larger models offer deeper reasoning, Gemini Flash excels in **real-time applications** where responsiveness and resource usage are key — making it a great fit for focused chatbots like this one.

---

## ✨ Features

- 🧠 Intent classification with 91% accuracy
- 🌍 Kosovo-specific Q&A using Gemini
- 🙋 Greetings and goodbyes support
- 🚫 Rejection of out-of-scope prompts
- ⚡ Fast, lightweight, and extensible

---

## 📁 Project Structure

```
.
├── app/
│   └── streamlist_app.py         # Streamlit chatbot app
├── data/
│   └── intent_data_fixed.csv     # Labeled training data
├── models/
│   ├── train_intent_classifier.py
│   ├── classifier_stats.py
│   └── intent_classifier.joblib
├── .env                          # Your API key lives here
├── requirements.txt
├── README.md
```

---

## 🖼️ Demo

![Kosovo Chatbot Demo](images/demo_image.png)

---

## 🖼️ Classifier Stats

![Classifier Stats](images/classifier_stats.png)

---

## 📜 License

MIT License

---

## 🙌 Contributions

Feel free to open issues or PRs. Contributions are welcome! 🇽🇰

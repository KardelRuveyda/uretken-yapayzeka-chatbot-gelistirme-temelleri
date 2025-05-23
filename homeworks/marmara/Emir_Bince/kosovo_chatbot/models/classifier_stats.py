from sklearn.metrics import classification_report
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data/chatbot_dataset.csv")
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['intent'], test_size=0.2, random_state=42)

train_intent_classifier = joblib.load("models/intent_classifier.joblib")

y_pred = train_intent_classifier.predict(X_test)
print(classification_report(y_test, y_pred, target_names=train_intent_classifier.classes_))

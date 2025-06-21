from sklearn.model_selection import train_test_split
import pandas as pd

# Excel dosyasını yükle
df = pd.read_excel("book_recommendation_dataset.xlsx")  # Excel dosyasındaki veriyi oku

# Sütun adlarını büyük harfli olarak alıyoruz
X = df['Example']    # Girdi cümleleri
y = df['Intent']     # Intent etiketleri

# Stratified split (Intent oranlarını koruyarak bölme)
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# DataFrame'lere dönüştür
train_df = pd.DataFrame({'Example': X_train, 'Intent': y_train})
test_df = pd.DataFrame({'Example': X_test, 'Intent': y_test})

# Excel olarak kaydet
train_df.to_excel("train.xlsx", index=False)
test_df.to_excel("test.xlsx", index=False)


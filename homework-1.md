# Zorluk Seviyesi: İleri Düzey - "Şifre Kırıcı" Problemi

## Senaryo
Bir hackerın bir sistemde kayıtlı **şifrelenmiş** bir mesajı çözmesi gerekiyor. Ancak, şifreleme belirli bir algoritma kullanılarak yapılmış. Senin görevin, bu algoritmayı tersine çevirerek **orijinal mesajı** ortaya çıkarmak.

---
## 🔐 Şifreleme Kuralları

1. **Her harf**, alfabede kendisinden **5 harf sonra** gelen harf ile değiştirilmiştir.  
   - Örnek: `"merhaba"` → `"rjwmfef"`  
   - Eğer harf **z'yi aşarsa**, alfabetik olarak başa döner. Örneğin: `"xyz"` → `"cde"`  

2. **Sayılar ters çevrilmiştir**.  
   - Örnek: `2024` → `4202`  

3. **Boşluklar ve noktalama işaretleri değiştirilmez**.  

---
## 🔑 Şifrelenmiş Mesaj

```
"ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
```

---
## 🎯 Görevler

✅ **Bu şifrelenmiş mesajı çöz (orijinal metni bul).**  
✅ **Python kullanarak tersine mühendislik yaparak algoritmayı ters çevir.**  
✅ **Bonus:** Kullanıcının kendi mesajını şifreleyip geri açabileceği bir program yaz.

## 📂 Proje Yapılandırması ve Teslim Kuralları

- **Öğrenciler, projeyi `homeworks` adlı klasörün içinde kendi üniversitelerine ait klasöre eklemelidir.**
- **Yıldız Teknik Üniversitesi (YTÜ) öğrencileri:**
  - `homeworks/ytu/` klasörünün içinde **kendi adlarından oluşan bir klasör** açmalı.
  - Örneğin, öğrenci adı **Ali Veli** ise:
    ```
    homeworks/
    ├── ytu/
    │   ├── Ali_Veli/
    │   │   ├── sifre_kirici.py
    ```
  - `sifre_kirici.py` dosyasına çözümlerini eklemeli.

- **Marmara Üniversitesi (Marmara) öğrencileri:**
  - Projeyi `homeworks/marmara/` klasörüne **fork** edip eklemelidir.
  - Örneğin, öğrenci adı **Ayşe Yılmaz** ise:
    ```
    homeworks/
    ├── marmara/
    │   ├── Ayse_Yilmaz/
    │   │   ├── sifre_kirici.py
    ```
  - `sifre_kirici.py` dosyası içinde kodlarını paylaşmalıdır.

## 🔄 GitHub'da Fork Nasıl Yapılır?

**Fork işlemi**, bir GitHub reposunun kopyasını kendi hesabınıza alarak üzerinde değişiklik yapabilmenizi sağlar. İşte adım adım nasıl yapacağınız:

1. **GitHub’a giriş yapın.**
2. **Ödevi içeren GitHub reposuna gidin.**
3. **Sağ üst köşede yer alan "Fork" butonuna tıklayın.**  
   - Bu işlem, projeyi kendi GitHub hesabınıza kopyalar.
4. **Kendi hesabınızdaki fork'lanan projeye gidin.**
5. **Projeyi kendi bilgisayarınıza klonlayın:**
   ```
   git clone https://github.com/kendi-kullanici-adiniz/orijinal-proje-adi.git
   ```
6. **Değişikliklerinizi yapın.**  
   - `homeworks/marmara/` içine **kendi adınızla** bir klasör açın.
   - Python çözümünüzü bu klasöre ekleyin (`sifre_kirici.py`).
7. **Yaptığınız değişiklikleri kaydedin ve yükleyin:**
   ```
   git add .
   git commit -m "Ödev tamamlandı - [Adınız]"
   git push origin main
   ```
8. **Pull Request (PR) gönderin:**
   - GitHub’a gidin, orijinal projeye geri dönün.
   - **"New Pull Request"** butonuna tıklayın.
   - Açılan sayfada, **kendi fork'unuzdaki değişiklikleri orijinal projeye önermek için** talepte bulunun.
   - Açıklama ekleyerek **Pull Request gönderin.**


## Ödev Teslim Tarihi
✅ **Teslim Tarihi YTU: 24.03.2024**
✅ **Teslim Tarihi Marmara: 27.03.2024**
 

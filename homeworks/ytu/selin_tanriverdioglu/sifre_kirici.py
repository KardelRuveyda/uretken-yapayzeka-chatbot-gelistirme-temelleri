#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string


# In[2]:


def sifreyi_coz(sifreli_metin):
    # Küçük harfler ve büyük harfleri tanımla
    kucuk_harfler = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
    buyuk_harfler = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Harfleri 5 karakter geri kaydırarak yeni alfabe oluştur
    cozulmus_kucuk_harfler = kucuk_harfler[-5:] + kucuk_harfler[:-5]  
    cozulmus_buyuk_harfler = buyuk_harfler[-5:] + buyuk_harfler[:-5]

    # Harfleri eski hallerine döndüren çeviri tablosunu oluştur
    donusum_tablosu = str.maketrans(kucuk_harfler + buyuk_harfler, cozulmus_kucuk_harfler + cozulmus_buyuk_harfler)

    # Harfleri eski haline döndür
    orijinal_metin = sifreli_metin.translate(donusum_tablosu)

    # Sayıları tersine çevir
    sonuc = ""
    for karakter in orijinal_metin:
        if karakter.isdigit():  # Eğer karakter bir sayıysa
            sonuc += karakter[::-1]  # Ters çevir
        else:
            sonuc += karakter  # Aynı bırak

    return sonuc


# In[3]:


# Test edelim
sifreli_metin = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
orijinal_metin = sifreyi_coz(sifreli_metin)
print("Çözülen Metin:", orijinal_metin)


# **Bonus**

# In[4]:


def sifrele(metin):
    # Alfabeleri tanımla (küçük ve büyük harfler)
    kucuk_harfler = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
    buyuk_harfler = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Harfleri 5 karakter ileri kaydırarak yeni alfabe oluştur
    sifreli_kucuk_harfler = kucuk_harfler[5:] + kucuk_harfler[:5]  
    sifreli_buyuk_harfler = buyuk_harfler[5:] + buyuk_harfler[:5]

    # Çeviri tablosunu oluştur (harfleri değiştirmek için)
    donusum_tablosu = str.maketrans(kucuk_harfler + buyuk_harfler, sifreli_kucuk_harfler + sifreli_buyuk_harfler)

    # Harfleri şifreleyelim
    sifreli_metin = metin.translate(donusum_tablosu)

    # Sayıları ters çevir
    sifrelenmis_sonuc = ""
    for karakter in sifreli_metin:
        if karakter.isdigit():  # Eğer karakter bir sayıysa
            sifrelenmis_sonuc += karakter[::-1]  # Sayıyı ters çevir
        else:
            sifrelenmis_sonuc += karakter  # Aynı bırak

    return sifrelenmis_sonuc


# In[5]:


def sifre_coz(sifreli_metin):
    # Aynı alfabeleri tekrar tanımla
    kucuk_harfler = string.ascii_lowercase
    buyuk_harfler = string.ascii_uppercase

    # Bu sefer harfleri **geri kaydırarak** eski hallerine döndür
    cozulmus_kucuk_harfler = kucuk_harfler[-5:] + kucuk_harfler[:-5]  
    cozulmus_buyuk_harfler = buyuk_harfler[-5:] + buyuk_harfler[:-5]

    # Harfleri geri çevirmek için çeviri tablosu oluştur
    donusum_tablosu = str.maketrans(kucuk_harfler + buyuk_harfler, cozulmus_kucuk_harfler + cozulmus_buyuk_harfler)

    # Harfleri eski haline döndür
    orijinal_metin = sifreli_metin.translate(donusum_tablosu)

    # Sayıları tekrar ters çevirerek eski hallerine getirelim
    cozulmus_sonuc = ""
    for karakter in orijinal_metin:
        if karakter.isdigit():  # Eğer karakter bir sayıysa
            cozulmus_sonuc += karakter[::-1]  # Sayıyı tekrar ters çevir
        else:
            cozulmus_sonuc += karakter  # Aynı bırak

    return cozulmus_sonuc


# In[6]:


# Kullanıcıya şifreleme mi çözme mi yapmak istediğini sor
print("Yapmak istediğiniz seçeneği seçin.")
print("1 - Metni şifrele")
print("2 - Şifreli metni çöz")

secim = input("Seçiminizi yapın (1 veya 2): ")

# Kullanıcıdan metin al
if secim == "1":
    metin = input("Şifrelenecek metni girin: ")
    sonuc = sifrele(metin)
    print("Şifrelenmiş Metin:", sonuc)

elif secim == "2":
    sifreli_metin = input("Çözülecek şifreli metni girin: ")
    sonuc = sifre_coz(sifreli_metin)
    print("Çözülen Metin:", sonuc)

else:
    print("Geçersiz seçim! Lütfen 1 veya 2 girin.")


# In[ ]:





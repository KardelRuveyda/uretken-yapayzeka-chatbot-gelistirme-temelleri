def harf_isle(karakter, kaydirma):      #merve hasaslari 170421922
    if karakter.isalpha():  #karakter bir harfse kontorl
        if karakter.islower():
            return chr((ord(karakter) + kaydirma - 97) % 26 + 97)
        else:
            return chr((ord(karakter) + kaydirma - 65) % 26 + 65)
    elif karakter.isdigit():  # karakter bir rakamsa kontrol
        return karakter[::-1]  # Rakamları ters çevirir buarad
    else:
        return karakter  # Boşluk ve noktalama işaretlerini olduğu gibi döndürme işlemini yapan kısım

def mesaj_coz(sifreli_metin):
    cozulmus_metin = ""
    for karakter in sifreli_metin:
        cozulmus_metin += harf_isle(karakter, -5)  #yukardaki fonksyonu kullanarak harfleri 5 geri alma işlemi
    return cozulmus_metin

def mesaj_sifrele(asil_metin):
    sifreli_metin = ""
    for karakter in asil_metin:
        sifreli_metin += harf_isle(karakter, 5)  # yukardaki fonksyonu kullanarak harfleri 5 geri alma işlemi
    return sifreli_metin

# verilen şifreli mesajı 
sifreli_metin = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
cozulmus_metin = mesaj_coz(sifreli_metin)
print("Çözülmüş Mesaj:", cozulmus_metin)

# kullanıcıdan mesaj alma ve şifreleme kısmı
kullanici_mesaji = input("Şifrelenecek mesajı girin: ")
sifreli_mesaj = mesaj_sifrele(kullanici_mesaji)
print("Şifrelenmiş Mesaj:", sifreli_mesaj)

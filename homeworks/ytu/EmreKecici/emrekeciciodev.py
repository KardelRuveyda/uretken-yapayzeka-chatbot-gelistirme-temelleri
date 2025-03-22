# Şifreli mesaj
sifreli_metin = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"

cozulmus_metin = ""
gecici_sayi = ""

for karakter in sifreli_metin:
    # Harfse
    if karakter.isalpha():
        # Eğer öncesinde sayı varsa onu ters çevirip ekle
        if gecici_sayi != "":
            cozulmus_metin += gecici_sayi[::-1]
            gecici_sayi = ""
        ascii_kodu = ord(karakter)
        yeni_kod = ascii_kodu - 5
        if yeni_kod < ord('a'):
            yeni_kod += 26
        cozulmus_metin += chr(yeni_kod)
    # Rakamsa biriktir
    elif karakter.isdigit():
        gecici_sayi += karakter
    else:
        # Sayı bitmişse tersini ekle
        if gecici_sayi != "":
            cozulmus_metin += gecici_sayi[::-1]
            gecici_sayi = ""
        # Harf ya da rakam değilse
        cozulmus_metin += karakter

# Mesajın sonunda sayı varsa ters çevirip ekle
if gecici_sayi != "":
    cozulmus_metin += gecici_sayi[::-1]

print(cozulmus_metin)

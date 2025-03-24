def sifre_coz(sifreli_metin):
    cozulmus_metin = ""
    i = 0
    while i < len(sifreli_metin): #mesaj sonuna kadar devam edecek döngü
        char = sifreli_metin[i]

        if char.isalpha(): #harf ise 5 karakter kayacak
            offset = ord('a')
            yeni_harf = chr((ord(char) - offset - 5) % 26 + offset)
            cozulmus_metin += yeni_harf
            i += 1

        elif char.isdigit(): #sayı ise ters çevirip eklenecek
            sayi = ""
            while i < len(sifreli_metin) and sifreli_metin[i].isdigit():
                sayi += sifreli_metin[i]
                i += 1
            cozulmus_metin += sayi[::-1]

        else: #sembol ise düz eklenecek
            cozulmus_metin += char
            i += 1

    return cozulmus_metin


def bonus_sifrele(metin):
    sifreli = ""
    i = 0
    while i < len(metin):
        char = metin[i]
        if char.isalpha():
            offset = ord('a')
            yeni_harf = chr((ord(char) - offset + 5) % 26 + offset)
            sifreli += yeni_harf
            i += 1
        elif char.isdigit():
            sayi = ""
            while i < len(metin) and metin[i].isdigit():
                sayi += metin[i]
                i += 1
            sifreli += sayi[::-1]
        else:
            sifreli += char
            i += 1
    return sifreli

def bonus_coz(metin):
    cozulmus = ""
    i = 0
    while i < len(metin):
        char = metin[i]
        if char.isalpha():
            offset = ord('a')
            yeni_harf = chr((ord(char) - offset - 5) % 26 + offset)
            cozulmus += yeni_harf
            i += 1
        elif char.isdigit():
            sayi = ""
            while i < len(metin) and metin[i].isdigit():
                sayi += metin[i]
                i += 1
            cozulmus += sayi[::-1]
        else:
            cozulmus += char
            i += 1
    return cozulmus


# şifreli "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl" mesajının çözülmesi

sifreli_metin = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
orijinal_metin = sifre_coz(sifreli_metin)
print("Çözülen Mesaj:", orijinal_metin)
print("\n")

# bonus soru için kullanıcıdan giriş alınması

while True:
    secim = input("\nBONUS SORU\n1- Şifrele\n2- Şifre Çöz\n0- Çıkış\nSeçiminiz: ")

    if secim == "0":
        print("Programdan çıkılıyor...")
        break

    elif secim == "1":
        girdi = input("Metni girin: ").lower()
        print("Şifreli Metin:", bonus_sifrele(girdi))

    elif secim == "2":
        girdi = input("Metni girin: ").lower()
        print("Çözülen Metin:", bonus_coz(girdi))

    else:
        print("Geçersiz seçim! Lütfen 1, 2 veya 0 girin.")

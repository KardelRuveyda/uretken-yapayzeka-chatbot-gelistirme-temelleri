# Çözme
def cozme(metin):
    cozulecek_kelime = ""
    for char in metin:
        if char.isalpha():  # Harf mi
            shift = -5  # Geri kaydırma
            if char.islower():
                cozulecek_kelime += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                cozulecek_kelime += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            cozulecek_kelime += char  # Harf değilse değiştirme
    return cozulecek_kelime

# Şifrelme 
def sifreleme(metin):
    sifrelenecek_kelime = ""
    for char in metin:
        if char.isalpha():
            shift = 5  # İleri kaydırma
            if char.islower():
                sifrelenecek_kelime += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                sifrelenecek_kelime += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            sifrelenecek_kelime += char
    return sifrelenecek_kelime

# Eğer şifrede sayı varsa tersine çevirme
def sayi_kurali(metin):
    return "".join(char if not char.isdigit() else "".join(reversed(char)) for char in metin)

# Şifreli metni çözme
sifreli_kelime = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
sifre_cozme = cozme(sifreli_kelime)
print("Çözülen mesaj:", sifre_cozme)

# Girilen metni şifreleme
girdi = input("Şifrelenecek mesajı girin: ")
metin_sifreleme = sifreleme(girdi)
print("Şifrelenmiş hali:", metin_sifreleme)

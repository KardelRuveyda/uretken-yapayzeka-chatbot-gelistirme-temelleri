import re

def sifre_cozme(sifreli_mesaj):
    cozulmus_mesaj = ""
    
    for char in sifreli_mesaj:
        if char.islower():  # Küçük harfler için
            new_char = chr(((ord(char) - ord('a') - 5) % 26) + ord('a'))
        elif char.isupper():  # Büyük harfler için
            new_char = chr(((ord(char) - ord('A') - 5) % 26) + ord('A'))
        else:
            new_char = char  # Harf değilse olduğu gibi bırak
        
        cozulmus_mesaj += new_char
    
    # sayıları terse çevirme
    cozulmus_mesaj = re.sub(r'\d+', lambda match: match.group()[::-1], cozulmus_mesaj)
    return cozulmus_mesaj

sifreli_mesaj = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl 1234"

cozulmus_mesaj = sifre_cozme(sifreli_mesaj)
print("Cozulmus mesaj:", cozulmus_mesaj)

def sifreleme(mesaj):
    sifreli_mesaj = ""
    for char in mesaj:
        if char.islower():  # Küçük harfler için
            new_char = chr(((ord(char) - ord('a') + 5) % 26) + ord('a'))
        elif char.isupper():  # Büyük harfler için
            new_char = chr(((ord(char) - ord('A') + 5) % 26) + ord('A'))
        else:
            new_char = char  # Harf değilse olduğu gibi bırak
        
        sifreli_mesaj += new_char
    
    # sayıları terse çevirme
    sifreli_mesaj = re.sub(r'\d+', lambda match: match.group()[::-1], sifreli_mesaj)
    return sifreli_mesaj

mesaj = "the quick brown fox jumps over the lazy dog 4321"

sifreli_mesaj = sifreleme(mesaj)
print("Sifrelenmis mesaj:", sifreli_mesaj)

islem_turu = input("\n-------- Sifreleme icin -> 1, Sifre cözme için -> 2 'e basın --------")
if islem_turu == '1':
    metin = input("Sifrelenecek metni girin")
    sifrelenmis_metin = sifreleme(metin)
    print("Metnin sifrelenmis hali : ", sifrelenmis_metin)
elif islem_turu == '2':
    metin = input("Cozulecek metni girin")
    cozulmus_metin = sifre_cozme(metin)
    print("Metnin cozulmus hali : ", cozulmus_metin)
else:
    print("Gecerli secenek girmediniz")
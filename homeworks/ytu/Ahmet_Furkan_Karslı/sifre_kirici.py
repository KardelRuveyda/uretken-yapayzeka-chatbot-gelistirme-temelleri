def sifreCoz(mesaj):
 sonuc = ""
 i = 0
 while i < len(mesaj):
  karakter = mesaj[i]
  if karakter.isalpha():
   sonuc += chr((ord(karakter) - ord('a') - 5) % 26 + ord('a'))
   i += 1
  elif karakter.isdigit():
   sayi = ""
   while i < len(mesaj) and mesaj[i].isdigit():
    sayi += mesaj[i]
    i += 1
   sonuc += sayi[::-1]
  else:
   sonuc += karakter
   i += 1
 return sonuc

def sifrele(mesaj):
 sonuc = ""
 i = 0
 while i < len(mesaj):
  karakter = mesaj[i]
  if karakter.isalpha():
   sonuc += chr((ord(karakter) - ord('a') + 5) % 26 + ord('a'))
   i += 1
  elif karakter.isdigit():
   sayi = ""
   while i < len(mesaj) and mesaj[i].isdigit():
    sayi += mesaj[i]
    i += 1
   sonuc += sayi[::-1]
  else:
   sonuc += karakter
   i += 1
 return sonuc

print("Çözülen Mesaj: ", sifreCoz("ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"))
kendi_mesaj = input("Mesajınızı girin: ")
print("Şifrelenmiş: ", sifrele(kendi_mesaj))
print("Tekrar Çözülmüş: ", sifreCoz(sifrele(kendi_mesaj)))
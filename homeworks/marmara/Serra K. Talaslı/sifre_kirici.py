def sifrele(metin):
    sonuc = ""
    for karakter in metin:
        if karakter.isalpha():
            ascii_deger = ord(karakter.lower())
            yeni_ascii = ascii_deger + 5
            if yeni_ascii > ord('z'):
                yeni_ascii = ord('a') + (yeni_ascii - ord('z') - 1)
            sonuc += chr(yeni_ascii)
        elif karakter.isdigit():
            sonuc += karakter[::-1]
        else:
            sonuc += karakter
    return sonuc

def coz(sifreli_metin):
    sonuc = ""
    for karakter in sifreli_metin:
        if karakter.isalpha():
            ascii_deger = ord(karakter.lower())
            yeni_ascii = ascii_deger - 5
            if yeni_ascii < ord('a'):
                yeni_ascii = ord('z') - (ord('a') - yeni_ascii - 1)
            sonuc += chr(yeni_ascii)
        elif karakter.isdigit():
            sonuc += karakter[::-1]
        else:
            sonuc += karakter
    return sonuc

def main():
    while True:
        print("\n1. Mesaj Şifrele")
        print("2. Şifreli Mesaj Çöz")
        print("3. Çıkış")
        
        secim = input("\nSeçiminiz (1-3): ")
        
        if secim == "1":
            metin = input("Şifrelenecek metni girin: ")
            sifreli = sifrele(metin)
            print(f"Şifrelenmiş metin: {sifreli}")
        
        elif secim == "2":
            sifreli_metin = input("Çözülecek şifreli metni girin: ")
            cozulmus = coz(sifreli_metin)
            print(f"Çözülmüş metin: {cozulmus}")
        
        elif secim == "3":
            print("Program sonlandırılıyor...")
            break
        
        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main() 
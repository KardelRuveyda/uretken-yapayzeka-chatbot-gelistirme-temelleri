def sifrele(mesaj):
    sonuc = ""
    for karakter in mesaj:
        if karakter.isalpha(): 
            ascii_deger = ord(karakter.lower())
            yeni_ascii = ((ascii_deger - ord('a') + 5) % 26) + ord('a')
            
            if karakter.isupper():
                sonuc += chr(yeni_ascii).upper()
            else:
                sonuc += chr(yeni_ascii)
        elif karakter.isdigit(): 
            sonuc += karakter
        else:  
            sonuc += karakter
    
    cikti = ""
    sayi_buffer = ""
    for karakter in sonuc:
        if karakter.isdigit():
            sayi_buffer += karakter
        else:
            if sayi_buffer:
                cikti += sayi_buffer[::-1]  
                sayi_buffer = ""
            cikti += karakter
    
    if sayi_buffer:
        cikti += sayi_buffer[::-1]
    else:
        cikti += sayi_buffer
        
    return cikti

def sifreyi_coz(sifrelenmis_mesaj):
    sonuc = ""
    for karakter in sifrelenmis_mesaj:
        if karakter.isalpha(): 
            ascii_deger = ord(karakter.lower())
            yeni_ascii = ((ascii_deger - ord('a') - 5) % 26) + ord('a')
            
            if karakter.isupper():
                sonuc += chr(yeni_ascii).upper()
            else:
                sonuc += chr(yeni_ascii)
        elif karakter.isdigit():  
            sonuc += karakter
        else:  
            sonuc += karakter
    cikti = ""
    sayi_buffer = ""
    for karakter in sonuc:
        if karakter.isdigit():
            sayi_buffer += karakter
        else:
            if sayi_buffer:
                cikti += sayi_buffer[::-1] 
                sayi_buffer = ""
            cikti += karakter
    
    if sayi_buffer:
        cikti += sayi_buffer[::-1]
    else:
        cikti += sayi_buffer
        
    return cikti

def main():
    print("Şifre Kırıcı / Şifreleyici Programı")
    print("====================================")
    
    while True:
        print("\nİşlem seçin:")
        print("1. Mesaj Şifrele")
        print("2. Şifreyi Çöz")
        print("3. Çıkış")
        
        secim = input("Seçiminiz (1-3): ")
        
        if secim == "1":
            mesaj = input("Şifrelenecek mesajı girin: ")
            sifrelenmis = sifrele(mesaj)
            print(f"Şifrelenmiş mesaj: {sifrelenmis}")
        
        elif secim == "2":
            sifre = input("Çözülecek şifreyi girin: ")
            cozulmus = sifreyi_coz(sifre)
            print(f"Çözülmüş mesaj: {cozulmus}")
        
        elif secim == "3":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")

if __name__ == "__main__":
    sifrelenmis_mesaj = "ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl"
    cozulmus_mesaj = sifreyi_coz(sifrelenmis_mesaj)
    print(f"Şifrelenmiş: {sifrelenmis_mesaj}")
    print(f"Çözülmüş: {cozulmus_mesaj}")
    
    main()
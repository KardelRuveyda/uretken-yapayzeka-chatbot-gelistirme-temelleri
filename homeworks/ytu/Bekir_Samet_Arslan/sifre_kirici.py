#Bekir Samet Arslan
def sifreyi_coz(sifreli_mesaj):
    cozulmus_mesaj = ""
    sayi_dizisi = ""
    sayi_mod = False
    
    for harf in sifreli_mesaj:
        if harf.isdigit():
            sayi_dizisi += harf
            sayi_mod = True
        else:
            if sayi_mod:
                cozulmus_mesaj += sayi_dizisi[::-1]
                sayi_dizisi = ""
                sayi_mod = False
            
            if harf.isalpha():
                harf_sirasi = ord(harf)
                yeni_harf = chr(harf_sirasi - 5)
                
                if yeni_harf < 'a':
                    yeni_harf = chr(ord(yeni_harf) + 26)
                    
                cozulmus_mesaj += yeni_harf
            else:
                cozulmus_mesaj += harf
    
    if sayi_mod:
        cozulmus_mesaj += sayi_dizisi[::-1]
    
    return cozulmus_mesaj

def sifrele(normal_mesaj):
    sifreli_mesaj = ""
    sayi_dizisi = ""
    sayi_mod = False
    
    for harf in normal_mesaj:
        if harf.isdigit():
            sayi_dizisi += harf
            sayi_mod = True
        else:
            if sayi_mod:
                sifreli_mesaj += sayi_dizisi[::-1]
                sayi_dizisi = ""
                sayi_mod = False
            
            if harf.isalpha():
                harf_sirasi = ord(harf)
                yeni_harf = chr(harf_sirasi + 5)
                
                if yeni_harf > 'z':
                    yeni_harf = chr(ord(yeni_harf) - 26)
                    
                sifreli_mesaj += yeni_harf
            else:
                sifreli_mesaj += harf
    
    if sayi_mod:
        sifreli_mesaj += sayi_dizisi[::-1]
    
    return sifreli_mesaj

while True:
    print("\n--- Şifreleme Programı ---")
    print("1. Mesaj Şifrele")
    print("2. Şifreli Mesajı Çöz")
    print("3. Programdan Çık")
    
    secim = input("\nNe yapmak istersiniz? (1/2/3): ")
    
    if secim == "1":
        mesaj = input("Şifrelenecek mesajı yazın: ")
        sonuc = sifrele(mesaj.lower())
        print("Şifrelenmiş mesaj:", sonuc)
        
    elif secim == "2":
        mesaj = input("Çözülecek şifreli mesajı yazın: ")
        sonuc = sifreyi_coz(mesaj.lower())
        print("Çözülmüş mesaj:", sonuc)
        
    elif secim == "3":
        print("Program kapatılıyor...")
        break
        
    else:
        print("Geçersiz seçim! Lütfen 1, 2 veya 3 girin.")

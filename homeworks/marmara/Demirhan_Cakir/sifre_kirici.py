class SifreKirici:
    def __init__(self, sifre="ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl", alfabe="abcdefghijklmnopqrstuvwxyz"):
        self.sifre = sifre
        self.alfabe = alfabe

    def sifreCoz(self): # Sifreli mesaj cozme fonksiyonu 
        secim = input("Ornek mesaji cozmek icin '1', Kendi mesajinizi cozmek icin '2': ")
        if secim == "1":
            sifre = self.sifre
        elif secim == "2":
            while True: # Girilen mesajin sadece harf ya da sadece rakam olup olmadigini kontrol eden dongu
                mesaj = input("Şifreli mesajı giriniz (sadece sayi ya da sadece harf giriniz!): ")
                try:
                    sayilar=0
                    harfler=0   
                    for kelime in mesaj.split(" "):
                        if kelime.isdigit():
                            sayilar=1
                        elif kelime.isalpha():
                            harfler=1
                    if sayilar==1 and harfler==0 or sayilar==0 and harfler==1:
                        sifre = mesaj
                        break
                    else:
                        print("\nGirilen mesaj hem harf hem de rakam içeriyor. Tekrar deneyin lütfen.\n")
                except Exception as e:
                    print(f"Hata oluştu: {e}") 
            
        alfabe = self.alfabe
        sifre = sifre.lower().split(" ")
        sifreCoz = []
        for kelime in sifre: # harfli mesajlar icin cozme islemi
            kelimeCoz = ""
            for harf in kelime:
                if harf in alfabe:
                    harfIndex = alfabe.index(harf)
                    harfIndex -= 5
                    if harfIndex < 0:
                        harfIndex += len(alfabe)
                    kelimeCoz += alfabe[harfIndex]
                else:
                    kelimeCoz += harf
            sifreCoz.append(kelimeCoz)
        
        if sifreCoz[-1].isdigit(): # sayili mesajlar icin mesaj cozme islemi 
            sifreCoz = sifreCoz[::-1]
            ters_kelimeler = [kelime[::-1] for kelime in sifreCoz]
            sifreCoz = ' '.join(ters_kelimeler)
        else:
            sifreCoz = ' '.join(sifreCoz)
        return "Mesajin sifresi cozulmus hali --> ",sifreCoz
        
    def mesajSifrelendir(self): # Mesaj sifreleme fonksiyonu
        while True: # Girilen mesajin sadece harf ya da sadece rakam olup olmadigini kontrol eden dongu
            mesaj = input("Şifrelenecek mesajı giriniz (sadece sayi ya da sadece harf giriniz!): ")
            try:
                sayilar=0
                harfler=0   
                for kelime in mesaj.split(" "):
                    if kelime.isdigit():
                        sayilar=1
                    elif kelime.isalpha():
                        harfler=1
                if sayilar==1 and harfler==0 or sayilar==0 and harfler==1:
                    sifre = mesaj
                    break
                else:
                    print("\nGirilen mesaj hem harf hem de rakam içeriyor. Tekrar deneyin lütfen.\n")
            except Exception as e:
                print(f"Hata oluştu: {e}") 
        alfabe = self.alfabe    
        mesaj = mesaj.lower().split(" ")
        sifre = []
        for kelime in mesaj: # harfli mesajlar icin sifreleme islemi
            kelimeSifre = ""
            for harf in kelime:
                if harf in alfabe:
                    harfIndex = alfabe.index(harf)
                    harfIndex += 5
                    if harfIndex >= len(alfabe):
                        harfIndex -= len(alfabe)
                    kelimeSifre += alfabe[harfIndex]
                else:
                    kelimeSifre += harf
            sifre.append(kelimeSifre)
        if sifre[-1].isdigit(): # sayili mesajlar icin sifreleme islemi
            sifre = sifre[::-1]
            ters_kelimeler = [kelime[::-1] for kelime in sifre] 
            sifre = ' '.join(ters_kelimeler)
        else:
            sifre = ' '.join(sifre)
        return "Mesajin sifrelenmis hali --> ",sifre


sifrekirici = SifreKirici()
print('\nOrnek sifreli mesaj: ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl \n')
print(sifrekirici.sifreCoz())
print('\n')
print(sifrekirici.mesajSifrelendir()) 

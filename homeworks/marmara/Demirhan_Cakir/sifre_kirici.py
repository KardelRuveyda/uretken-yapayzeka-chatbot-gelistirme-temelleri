class SifreKirici:
    def __init__(self, sifre="ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl", alfabe="abcdefghijklmnopqrstuvwxyz"):
        self.sifre = sifre
        self.alfabe = alfabe

    def sifreCoz(self):
        secim = input("Ornek mesaji cozmek icin '1', Kendi mesajinizi cozmek icin '2': ")
        if secim == "1":
            sifre = self.sifre
            alfabe = self.alfabe
            sifre = sifre.lower()
            sifre = sifre.split(" ")
            sifreCoz = []
            for kelime in sifre:
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
            sifreCoz = ' '.join(sifreCoz)
            return sifreCoz
        
        elif secim == "2":
            mesaj = input("Şifreli mesajı giriniz: ")
            self.mesaj = mesaj
            alfabe = self.alfabe
            mesaj = mesaj.lower()
            mesaj = mesaj.split(" ")
            sifreCoz = []
            for kelime in mesaj:
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
            sifreCoz = ' '.join(sifreCoz)
            return sifreCoz
        
    
    def mesajSifrelendir(self):
        mesaj = input("Sifrelenecek mesaji giriniz: ")
        alfabe = self.alfabe    
        mesaj = mesaj.lower()
        mesaj = mesaj.split(' ')
        sifre = []
        for kelime in mesaj:
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
        sifre = ' '.join(sifre)
        return sifre


sifrekirici = SifreKirici()
print('\nOrnek sifreli mesaj: ymj vznhp gwtbs ktc ozrux tajw ymj qfed itl \n')
print(sifrekirici.sifreCoz())
print('\n')
print(sifrekirici.mesajSifrelendir()) 
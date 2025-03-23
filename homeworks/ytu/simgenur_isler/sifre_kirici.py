alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def önceki_harf(harf):
    if harf in alfabe:
        index = alfabe.index(harf)
        yeni_index = (index - 5) % len(alfabe)
        return alfabe[yeni_index]
    return harf

def sayiyi_tersine_cevir(sayi_str):
    return sayi_str[::-1]

def orijinalmesajıbul(sifre):
  cozulmus_sifrel = []
  sayi = ""

  for i in sifre:
      if i.isdigit():
          sayi += i
      elif i == ' ':
          if sayi:
              cozulmus_sifrel.append(sayiyi_tersine_cevir(sayi))
              sayi = ""
          cozulmus_sifrel.append(' ')
      else:
          if sayi:
              cozulmus_sifrel.append(sayiyi_tersine_cevir(sayi))
              sayi = ""
          y = önceki_harf(i)
          cozulmus_sifrel.append(y)

  if sayi:
      cozulmus_sifrel.append(sayiyi_tersine_cevir(sayi))

  cozulmus_sifre= ''.join(cozulmus_sifrel)
  print(cozulmus_sifre)
  orijinalmesajıbul("ymj 4572 vznhp gwtbs ktc ozrux tajw ymj qfed itl")
  def sonraki_harf(harf):
    if harf in alfabe:
        index = alfabe.index(harf)
        yeni_index = (index + 5) % len(alfabe)
        return alfabe[yeni_index]
    return harf

def sifrelenmismesajıbul(sifre):
  cozulmus_sifrel = []
  sayi = ""

  for i in sifre:
      if i.isdigit():
          sayi += i
      elif i == ' ':
          if sayi:
              cozulmus_sifrel.append(sayiyi_tersine_cevir(sayi))
              sayi = ""
          cozulmus_sifrel.append(' ')
      else:
          if sayi:
              cozulmus_sifrel.append(sayiyi_tersine_cevir(sayi))
              sayi = ""
          y = sonraki_harf(i)
          cozulmus_sifrel.append(y)

  if sayi:
      cozulmus_sifrel.append(sayiyi_tersine_cevir(sayi))

  cozulmus_sifre= ''.join(cozulmus_sifrel)
  print(cozulmus_sifre)
  sifrelenmismesajıbul("the 654 quick brown fox jumps over the lazy dog")

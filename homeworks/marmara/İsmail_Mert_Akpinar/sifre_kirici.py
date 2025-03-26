{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "029fc089-46d1-4ca2-bcc3-d7e1da29268c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sifreli mesaj:  nxrfnq rjwy fpunsfw\n",
      "Cözülmüs hali :  ismail mert akpinar\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Sifrelemek istediginiz mesaji giriniz:  merhaba\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sifrelenmis hali: rjwmfgf\n"
     ]
    }
   ],
   "source": [
    "def harf_coz(harf):\n",
    "    alfabe = \"abcdefghijklmnopqrstuvwxyz\"\n",
    "    if harf in alfabe:\n",
    "        eski_index = alfabe.index(harf)\n",
    "        yeni_index = (eski_index - 5) % 26\n",
    "        return alfabe[yeni_index]\n",
    "    else:\n",
    "        return harf\n",
    "\n",
    "def sifre_coz(metin):\n",
    "    sonuc = \"\"\n",
    "    for karakter in metin:\n",
    "        sonuc += harf_coz(karakter)\n",
    "    return sonuc\n",
    "\n",
    "def harf_sifrele(harf):\n",
    "    alfabe = \"abcdefghijklmnopqrstuvwxyz\"\n",
    "    if harf in alfabe:\n",
    "        eski_index = alfabe.index(harf)\n",
    "        yeni_index = (eski_index + 5) % 26\n",
    "        return alfabe[yeni_index]\n",
    "    else:\n",
    "        return harf\n",
    "\n",
    "def mesaj_sifrele(metin):\n",
    "    sonuc = \"\"\n",
    "    for karakter in metin:\n",
    "        sonuc += harf_sifrele(karakter)\n",
    "    return sonuc\n",
    "\n",
    "sifreli = \" nxrfnq rjwy fpunsfw\" \n",
    "\n",
    "cozulmus = sifre_coz(sifreli)\n",
    "print(\"Sifreli mesaj:\", sifreli)\n",
    "print(\"Cözülmüs hali :\", cozulmus)\n",
    "\n",
    "kendi_mesaji = input(\"Sifrelemek istediginiz mesaji giriniz: \")\n",
    "print(\"Sifrelenmis hali:\", mesaj_sifrele(kendi_mesaji))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ee0827b-cf2f-4f01-b65d-00c9dc14e25b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.11"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

#!/usr/bin/python3

import os 
from zipfile import ZipFile

def zipacıcı(zipadi):

    for sayac in range(500):
        with ZipFile(zipadi, "r") as rarDosya:
            iceridekiDosyadı = rarDosya.namelist()
            sifre = iceridekiDosyadı[0].split(".")

            rarDosya.extractall(pwd = bytes(sifre[0], 'utf-8'))
            # os.remove(zipadi)
            sayac += 1
            print(f"{sayac}. Dosya açıldı. Şifre {sifre[0]} ")
            zipadi = iceridekiDosyadı[0]    # zipacıcı(iceridekiDosyadı[0])

zipacıcı(str(input("Zip dosyasının adını gir= ")))

# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:29:23 2024

@author: Monster
"""
from multiprocessing import Process
import os
import time


def islem_yap(sayi):
    print(f"İşlemci: {os.getpid()} - Sayi: {sayi}, Küp: {sayi * sayi * sayi}")
    time.sleep(2) 
    
if __name__ == "__main__":
    print("Çoklu İşlemci (Multiprocessing) Başlıyor...")
    
    sayilar = [2,4,6]
    islemler = []
    
    # Her sayı için ayrı bir işlem oluştur 
    for sayi in sayilar:
        islem = Process(target=islem_yap, args=(sayi,))
        islemler.append(islem)
        islem.start()
        
    for islem in islemler:
        islem.join()
        
    print("Tüm işlemler tamamlandı!")
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 17:17:15 2024

@author: Monster
"""

import time

def program1():
    for i in range(5):
        print(f"Program1 çalışıyor: {i}")
        time.sleep(1)
        
def program2():
    for i in range(5):
        print(f"Program2 çalışıyor: {i}")
        time.sleep(1)
        
def program3():
     for i in range(5):
         print(f"Program3 çalışıyor: {i}")
         time.sleep(1)
         
if __name__ == "__main__": 
    import threading
    
    # "__" string demekmişşş.
    # 3 programı aynı anda çalıştırıyorum...
    thread1 = threading.Thread(target=program1)
    thread2 = threading.Thread(target=program2)
    thread3 = threading.Thread(target=program3)
    
    thread1.start()
    thread2.start()
    thread3.start()
    
    thread1.join()
    thread1.join()
    thread1.join()
    
    print("Tüm porgramlar aynı anda çalışıyor gibi ancaaaak sırayla çalışıyorlar.")
    
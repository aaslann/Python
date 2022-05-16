# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:43:14 2022

@author: abdurrahman.aslan
"""

from collections import Counter

myList = ["BELİRGİN","CİHANGİR","ÇİLİNGİR","DİRENGEN","DRİPLİNG",
"ERGENLİK","ERGİNLİK","ERGONOMİ","ERGUVANİ","ETTİRGEN",
"FİLİGRAN","FRENGİLİ","GABARDİN","GARDİYAN","GARNİTÜR",
"GARNİZON","GEÇİRGEN","GERGİNCE","GERİNMEK","GİRİŞKEN",
"GLİSERİN","GÖNDERİM","GÖNDERİŞ","GÖNDERLİ","GRANÜLİN",
"GRANÜLİT","GÜVERCİN","HERHANGİ","İĞRENGEN","İNDİRGEN",
"İNTEGRAL","KEMİRGEN","MARGARİN","ORGANİZE","ORGANTİN",
"REDİNGOT","SEMİRGİN","SÜNGERCİ","SÜNGERLİ","SÜNGERSİ","TEDİRGİN"]

i=0
while i < len(myList):
    
    my_str = myList[i]
    counter = Counter(my_str)

    if counter['İ'] == 2:
        print(myList[i])
        
    i+=1
 

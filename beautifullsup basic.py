# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 20:47:59 2021

@author: peppi
"""

#parser con beautifullsup

from bs4 import BeautifulSoup
import requests
import html5lib

url="http://www.basilicasanmarco.it"

risposta=requests.get(url)
print(risposta.text)  #♣con .text ho html

dati=risposta.text

beautifullsup=BeautifulSoup(dati,"html5lib")  #gli passo la pagina salvata a beautiful con il linguaggio html cosi posso lavorare direttamente su
                                                #questa pagina
                                                
for link in beautifullsup.find_all("a"):
    print(link)

for form in beautifullsup.find_all("form"):
    print(form)


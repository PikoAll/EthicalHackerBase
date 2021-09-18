# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 20:28:27 2021

@author: peppi
"""

#andiamo a estrapolare tutti i link presenti in una pagina web
#parsing=analisi

from html.parser import HTMLParser
import urllib.request

risposta=urllib.request.urlopen("http://www.basilicasanmarco.it")
stringa=risposta.read()
stringa=str(stringa)

print(stringa)
print("###################################################")

class MiaClasseParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        
        if( tag == "a"):     #sto analizzando i tag di a dove dentro ce un link possiamo prendere tutti i tag che vogliamo 
            
            for name,value in attrs:
                if(name=="href"):
                    print(value)
                    

mioParser=MiaClasseParser()
mioParser.feed(stringa)
                




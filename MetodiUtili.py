# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:44:02 2021

@author: peppi
"""

#METODI UTILI
import socket

stringa=socket.gethostbyname("google.it") #cosi otteniamo l'indirizzo ip assocciato a google.it
print(stringa)

stringa=socket.gethostbyname_ex("google.it") #questo medoto serve per vedere piu di un indirizzo associato a google
print(stringa)

stringa=socket.gethostbyaddr("8.8.8.8") #abbiamo messo i dns di google ora in stringa ci sara salvato google.it
print(stringa)


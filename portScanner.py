# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#portScanner solo per LINUX

import nmap

primoPortScanne=nmap.PortScanner()

print(dir(primoPortScanne))   #mi stampa tutte le funzionalita che posso fare
print("#########################")
#passimo l'ip del dispositivo e la porta da analizzare, l'ultimo parametro e il tipo di scansione che facciamo
#posso passare piu porte per esempio "22,80,53" 
primaScansione=primoPortScanne.scan("10.0.2.15","23","sS")
print(primaScansione)
print("3333333333333333333333333333")

#manipoliamo meglio l'output
print(primoPortScanne.command_line()) #per stampare meglio quello che ci serve
print(primoPortScanne.scaninfo())

#
print("44444444444444444444444444444")
print(primoPortScanne["10.0.2.15"].state())

stringa=primoPortScanne["10.0.2.15"].state()

if stringa=="up":
    print("host attivo")
else:
    print("host inattivo")


print(primoPortScanne["10.0.2.15"]["tcp"].keys()) #ci restituisce le porte

 


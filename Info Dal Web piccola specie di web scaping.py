# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:40:02 2021

@author: peppi
"""

import http.client

conessione=http.client.HTTPConnection("www.httpbin.org")

conessione.request("GET", "/forms/post")  #faccio la richiesta al sito

rispostaServer=conessione.getresponse() #prendo la risposta

print(rispostaServer)
print(rispostaServer.status, rispostaServer.reason)

dati=rispostaServer.read()
print(dati.decode())


print("#######################################################")

import urllib.request

try:
    risposta=urllib.request.urlopen("http://www.google.it")
    print(risposta.read())
    print("#############################•22222222222222222222222222222222###########☻")
    risposta.close()

except urllib.request.URLError as errore:
    print(errore.reason)

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:05:15 2021

@author: peppi
"""

#CLIENTE TCP

# Creazione CLIENT SOCKET:
#--------------------------------
# 1 - Creazione socket                      # socket.socket()
# 2 - Connessione al Server                 # connect(indirizzo)
# 3 - Invio di una Richiesta al Server      # send()
# 4 - Ricezione della Risposta dal Server   # recv()
# Funzioni Generiche:
#--------------------------------
# s.recv()                => Riceve messaggi TCP
# s.send()                => Trasmette messaggi TCP
# s.close()               => Chiude il Socket
# socket.gethostname()    => Restituisce l'hostname della macchina su cui sta girando l'Interprete di Python
# socket.gethostbyname()  => Restituisce l'IP associato al nome passato



import sys
import socket


'''
socketClient=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host="127.0.0.1"  #indirizzo del server
port=9898

socketClient.connect((host,port))

#ora inviamo messaggio al client
socketClient.send(b"Ciao server")

request=socketClient.recv(1024) #ricevo buffer grandezza 1024

print("Ho ricevuto dal server ", request.decode())

socketClient.close()
'''




def conessioneServer(indirizzoServer):
    
    try:
        s=socket.socket()
        s.connect(indirizzoServer)
        print("conessione avvenuta con: ",indirizzoServer)
    
    except socket.error as errore:
        print('Qualcosa e andato storto sto chiudento')
        sys.exit()
        
    #invio dei dati e ricevo
    s.send(b"ciao Server")    #invio dati
    request=s.recv(4096)    #ricevo dati massima lunghezza buffer 4096
    print("ho ricevuto dal server: ",request.decode())
    s.close()
    
    

conessioneServer(("127.0.0.1",9898)) #passo l'indirizzo del server e la porta
    










 
    
    
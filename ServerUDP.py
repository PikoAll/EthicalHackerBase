# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:20:33 2021

@author: peppi
"""

import socket
import sys

host="127.0.0.1"
port=12345

socketServer=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    
    socketServer.bind((host,port))
    socketServer.settimeout(10) #dopo 10 secondi si chiude il Server
        
    print("server in ascolto..")
    
    dati,addr=socketServer.recvfrom(1024)  #grandezza buffer da ricevere
    
    print("SERVER: ho ricevuto da questo indirizzo ",addr," questa frase: ",dati.decode())
    socketServer.close()

except socket.timeout :
    print("nessuna conessione avvenuta io chiudo")
    socketServer.close()
    sys.exit()

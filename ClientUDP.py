# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:30:37 2021

@author: peppi
"""

import socket


host="127.0.0.1"
port=12345


socketClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

socketClient.sendto(b"Client: ciao Server come va?", (host,port))
print("Nessun problema di conessione")

socketClient.close()




# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 11:13:27 2021

@author: peppi
"""

#SERVER TCP

# Creazione CLIENT SOCKET:
#--------------------------------
# 1 - Creazione socket                      # socket.socket()
# 2 - Connessione al Server                 # connect(indirizzo)
# 3 - Invio di una Richiesta al Server      # send()
# 4 - Ricezione della Risposta dal Server   # recv()

# Creazione SERVER SOCKET:
#--------------------------------
# 1 - Creazione socket                                                              # socket.socket()
# 2 - Collegamento del socket all'indirizzo della macchina e alla Porta Designata   # bind()
# 3 - Messa in ascolto in attesa della connessione del Client                       # listen()
# 4 - Accettazione del Client                                                       # accept()
# 5 - Ricezione Richiesta dal Client                                                # recv()
# 4 - Elaborazione di una Risposta                                                  # subprocess()
# 5 - Invio Risposta al Client  


import socket
import subprocess
import sys


'''
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host="127.0.0.1"   #indirizzo ip del server
port=9898

serverSocket.bind((host,port))
serverSocket.listen(4)  #4 numero di conessione che vogliamo 

clientSocket, addres=serverSocket.accept()
print("conessione avvenuta con", clientSocket,"  ",addres)
request=clientSocket.recv(1024)  #1024 dimensione del buffer ricevuto

print("ho ricevuto dal client questo messaggio ", request.decode())

clientSocket.send(b"ho ricevuto il messagio grazie client")  #invio messaggio al client



'''
def inizializzoServer(indirizzo, backlog=1):
    
  
            s=socket.socket()
            s.bind(indirizzo)
            s.listen(4)  #4 numero di conessione che vogliamo 
            print("server in ascolto")
        
        
            while True:
                conn,indirizzoClient=s.accept()
                #print("conessione con client stabilita con address", indirizzoClient ," ",conn)
                print("conessione con client stabilita con address", indirizzoClient )
          
                request=conn.recv(4096)   #4096 dimensione del buffer ricevuto
                #request = subprocess.run(richiesta.decode(), shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
                print("ho ricevuto dal client ",request.decode())
                conn.send(b"Ho ricevuto il tuo messaggio client io Sono IL SERVER")
        
        
        
inizializzoServer(("127.0.0.1",9898))  #porta e indirizzo del server












#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:40:56 2021

@author: kali
"""
# il file in riga host_key=paramiko.RSAKey(filename="test_rsa.key") deve contenere queste cose incollate qua sotto
'''
-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgQDTj1bqB4WmayWNPB+8jVSYpZYk80Ujvj680pOTh2bORBjbIAyz
oWGW+GUjzKxTiiPvVmxFgx5wdsFvF03v34lEVVhMpouqPAYQ15N37K/ir5XY+9m/
d8ufMCkjeXsQkKqFbAlQcnWMCRnOoPHS3I4vi6hmnDDeeYTSRvfLbW0fhwIBIwKB
gBIiOqZYaoqbeD9OS9z2K9KR2atlTxGxOJPXiP4ESqP3NVScWNwyZ3NXHpyrJLa0
EbVtzsQhLn6rF+TzXnOlcipFvjsem3iYzCpuChfGQ6SovTcOjHV9z+hnpXvQ/fon
soVRZY65wKnF7IAoUwTmJS9opqgrN6kRgCd3DASAMd1bAkEA96SBVWFt/fJBNJ9H
tYnBKZGw0VeHOYmVYbvMSstssn8un+pQpUm9vlG/bp7Oxd/m+b9KWEh2xPfv6zqU
avNwHwJBANqzGZa/EpzF4J8pGti7oIAPUIDGMtfIcmqNXVMckrmzQ2vTfqtkEZsA
4rE1IERRyiJQx6EJsz21wJmGV9WJQ5kCQQDwkS0uXqVdFzgHO6S++tjmjYcxwr3g
H0CoFYSgbddOT6miqRskOQF3DZVkJT3kyuBgU2zKygz52ukQZMqxCb1fAkASvuTv
qfpH87Qq5kQhNKdbbwbmd2NxlNabazPijWuphGTdW0VfJdWfklyS2Kr+iqrs/5wV
HhathJt636Eg7oIjAkA8ht3MQ+XSl9yIJIS8gVpbPxSw5OMfw0PjVE7tBdQruiSc
nvuQES5C9BMHjF39LZiGH1iLQy7FgdHyoP+eodI7
-----END RSA PRIVATE KEY-----

'''

#SSH e un protocollo sicuro e cifrato


import paramiko
import socket
import threading
import warnings
import subprocess

warnings.filterwarnings(action="ignore",module=".*paramiko.*")  #per evitare i worning rilasciati da paramiko

host_key=paramiko.RSAKey(filename="test_rsa.key")

class Server (paramiko.ServerInterface):
    
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if (username == "pippo") and (password == "pippo123456"):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
    

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("10.0.2.15",22))
sock.listen(10)  #massimo 10 conessioni
client,addr=sock.accept()
print("conessione instaurata")

#entriamo in merito al protocolo ssh
t=paramiko.Transport(client)  
t.add_server_key(host_key)

server=Server()
t.start_server(server=server)

chan=t.accept(20)
print("il client e autenticato")

command=chan.recv(1024) #ricevo 1024 digradezza massima

command=str(command,"utf-8")

print(command)   #posso ricevere anche stinghe oltre a comandi di terminale

CMD=subprocess.check_output([command],shell=True)
CMD=str(CMD)
print(CMD)

#ora invia il server invia il comando al client
command="ls"
chan.send(command)

#ora ricevo
request=chan.recv(1024)
print(request)

t.close()




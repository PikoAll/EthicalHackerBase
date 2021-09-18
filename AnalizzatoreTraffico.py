#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 16:00:12 2021

@author: kali
"""

import socket,struct,binascii

s=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.ntohs(0x0800))

while True:
    #pacchetto=s.recv(65565)
    pacchetto=s.recvfrom(65565)
    #print(pacchetto)  #stampa troppe cose a prima vista sensa senzo lo metto sotto comento
    #print("############################")
    
    #estrapoliamo una porzione di pacchetto 
    #livello 2 ISo oSI
    pacchetto2=pacchetto[0][0:14]
    pacchetto3=struct.unpack("!6s6sH",pacchetto2)
    
    src_mac=binascii.hexlify(pacchetto3[1]) #surse mac
    dst_mac=binascii.hexlify(pacchetto3[0]) #destinascion mac
    eth_type=pacchetto3[2] #ethernet type
    
    data={"Destination MAC": dst_mac,"Surce MAC": src_mac, "protocollo ETH":eth_type}
    print(data)
    
    
    print("IP Header")
    #livello 3 ISo oSI
    ipHeader=pacchetto[0][14:34]
    pacchetto4=struct.unpack("!12s4s4s",ipHeader)
    print("Source IP       ->      Destination IP")
    print(socket.inet_ntoa(pacchetto4[1]), "-->",socket.inet_ntoa(pacchetto4[2]) )
    
    #livello 4 ISO OSI
    tcpHeader=pacchetto[0][34:54]
    pacchetto5=struct.unpack("!HH9sB6s", tcpHeader)
    print("TCP Header")
    print("Source Port       ->      Destination Port")
    print(pacchetto5[0],"   -->  ",pacchetto5[1])
    
    
    
    
    
    
    
    
    
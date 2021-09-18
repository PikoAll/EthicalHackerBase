# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:01:50 2021

@author: peppi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:45:26 2021

@author: kali
"""

import pyscreenshot as ImageGrab
from pathlib import Path

#prende tutto lo scermo
def ottieni_fullscreen(percorso):
    immaggine=ImageGrab.grab()
    immaggine.save(percorso)
    print("screenschot  totale fatto")
    
    
#prende una parte dello scermo
def ottieni_screeParziale(sx,alto,dx,basso,percorso):
    
    immaggine=ImageGrab.grab(bbox=(sx,alto,dx,basso))
    immaggine.save(percorso)
    print("screenschot  parziale fatto")
    





immaggine=ImageGrab.grab()
immaggine.save("screen.png")

percorsoFile="/home/kali/Desktop/"
percorso=Path("screen2.png")
percorso.touch()

ottieni_fullscreen(str(percorso.resolve()))

percorsoParziale=Path("screenParziale.png")
percorsoParziale.touch()
ottieni_screeParziale(0,100,500,500,str(percorsoParziale.resolve()))






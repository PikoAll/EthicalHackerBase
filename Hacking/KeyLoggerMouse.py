# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:44:53 2021

@author: peppi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:38:25 2021

@author: kali
"""

from pynput.mouse import Listener

#si puo anche inserirere le cordinate del mouse.....

def onClik(x,y,tasto, premuto):
    if premuto:
        print("click del mouse rilevato con il tasto ", format(tasto))
        

with Listener(
        on_click=onClik
        )as listener:
    listener.join()
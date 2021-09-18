# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 18:17:36 2021

@author: peppi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 12:03:08 2021

@author: kali
"""

#c'e qualche errore

import pygame.camera 



screen=pygame.display.set_mode([800,400])  #setto dimesioni foto forse

#inizializzo webcam
pygame.init()
pygame.camera.init()


cameras = pygame.camera.list_cameras()
print ("Using camera %s ..." % cameras[0], cameras)
miaCamera = pygame.camera.Camera(cameras[0],(800,400))


#miaCamera=pygame.camera.Camera("dev/Video0", (640,480))  #carico fotocamera
miaCamera.start()
immagine=miaCamera.get_image() 

screen.fill([0,0,0])
screen.blit(immagine,(100,0))

pygame.display.update()
pygame.image.save(immagine,"immagineWbCam.png")






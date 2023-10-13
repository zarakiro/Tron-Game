import queue
import pygame
import sys
from modules.network_client import NetworkClient
from modules.capture_input import CaptureInput
from modules.rendering import Rendering
from modules.player import Player

IP_ADRESSE="172.21.72.228"
PORT=2221


pygame.init()
ntw=NetworkClient(IP_ADRESSE,PORT)
input=CaptureInput(ntw)
a=True
render=Rendering()

while a:
    # for event in pygame.event.get():
        # if event.type==pygame.QUIT:
        #     render.close()
        #     input.stop()
        #     ntw.close()
        #     sys.exit()
        #     a=False

    render.affichage(ntw.players)

input.stop()
ntw.close() 
pygame.quit()
sys.exit()


        

import pygame
from pygame.locals import *
import threading
import sys
from modules.network_client import NetworkClient



class CaptureInput():

    def __init__(self, ntw : NetworkClient) -> None:
        pygame.init()
        self.run = True
        self.ntw=ntw   
        self.thread = threading.Thread(target=self._thread_target) 
        self.start()

    def _thread_target(self):
        pygame.init()
        while self.run :
            key_input = pygame.event.wait()
            if key_input.type==QUIT:
                pygame.quit()
            elif key_input.type==KEYDOWN:
                if key_input.key==K_UP:
                    self.ntw.sending_queue.put("key,UP")
                if key_input.key==K_DOWN:
                    self.ntw.sending_queue.put("key,DOWN")
                if key_input.key==K_LEFT:
                    self.ntw.sending_queue.put("key,LEFT")
                if key_input.key==K_RIGHT:
                    self.ntw.sending_queue.put("key,RIGHT")
            

    def start(self):
        self.thread.start()
    
    def stop(self):
        self.run = False
        self.thread.join(1)

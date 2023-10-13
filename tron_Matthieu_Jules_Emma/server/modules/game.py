import pygame
from modules.player import Player
from modules.network_server import NetworkServer
import threading

POS_DEPART=[(30,570),(770,30),(30,30),(770,570)]
DIRECTION_DEPART=[(1, 0),(-1, 0),(1, 0),(-1, 0)]
COULEURS_JOUEURS=[(0, 255, 255),(255, 228, 54),(77,239,12),(255,0,0)]
class Game:

    def __init__(self,ntw:NetworkServer):
        self.largeur=800
        self.hauteur=600
        self.players : dict[str : Player]={}
        self.victoire=False
        self.ntw = ntw
        self.run=True

        self.event_thread=threading.Thread(target=self._event_thread_target)
        self.event_thread.start()

        pass

    def _event_thread_target(self):
        while self.run:
            data = self.ntw.get_event_queue().get()
            self.msg_rcv_callback(data)

    def msg_rcv_callback(self,data:tuple):#data est un tuple contenant d'abord Ip puis msg reçu
        msg=data[1].split(',')
        if msg[0] == 'new_player':
            player_nb = len(self.players)
            self.players.update({data[0] : Player(POS_DEPART[player_nb][0],POS_DEPART[player_nb][1],DIRECTION_DEPART[player_nb],COULEURS_JOUEURS[player_nb])})
        # elif data[0] == 'pos':
        #     self.players[ip_player].update_pos(())
        elif msg[0] == 'key':
             # self.set_direction(self.players[ip_player],data[1])
            if msg[1]=="LEFT" and self.players[data[0]].direction != (1, 0):
                self.players[data[0]].direction=(-1, 0)
            if msg[1]=="RIGHT" and self.players[data[0]].direction != (-1, 0):
                self.players[data[0]].direction=(1, 0)
            if msg[1]=="UP" and self.players[data[0]].direction != (0, 1):
                self.players[data[0]].direction=(0, -1)
            if msg[1]=="DOWN" and self.players[data[0]].direction != (0, -1):
                self.players[data[0]].direction=(0, 1)
               

    def jeu(self):
        player_to_send = {}
        for key in self.players:
            if not self.collisions_murs(self.players[key]) and not self.collisions_traine(self.players[key]):
                self.players[key].update_pos()
                self.players[key].update_traine()
            player_to_send.update({key : self.players[key].serialize()})
        if len(player_to_send) != 0: 
            self.ntw.sendall(player_to_send)

                
        



        
    # def set_direction(self, player:Player, key_input:str):
    #     if not self.collisions_murs(player) and not self.collisions_traine():
    #         if key_input=="LEFT" and player.direction != (1, 0):
    #             player.direction  = (-1, 0)
    #         elif key_input=="RIGHT" and player.direction  != (-1, 0):
    #             player.direction  = (1, 0)
    #         elif key_input=="UP" and player.direction  != (0, 1):
    #             player.direction  = (0, -1)
    #         elif key_input=="DOWN" and player.direction  != (0, -1):
    #             player.direction = (0, 1)


    def collisions_murs(self,player1:Player):
            #Verif collisions avec limites
        if(player1.x < 0 or player1.x >= self.largeur or player1.y < 0 or player1.y >= self.hauteur): 
            self.victoire=True       
            return True
        return False
    
    def collisions_traine(self,player1:Player):
            # Verif collisions avec traînées
        for joueur in self.players.values():
            if (player1.x, player1.y) in joueur.traine:
                self.victoire=True 
                return True
        return False
    
    def GetVictoire(self):
        return self.victoire

        
        
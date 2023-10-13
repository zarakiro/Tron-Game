import pygame
import sys
from modules.player import Player


noir=(0,0,0)
blanc=(255,255,255)   
bleu_titre=(121, 248, 248)
image_moto_joueur = pygame.image.load("moto.png")
largeur_moto = 50
hauteur_moto = 40
image_moto_joueur = pygame.transform.scale(image_moto_joueur, (largeur_moto, hauteur_moto))


class Rendering():

    def __init__(self):
        # pygame.init()
        self.largeur=800   
        self.hauteur=600
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Light Racer")
        font = pygame.font.Font(None, 36)  
        self.vitesse = 2.5
        self.clock = pygame.time.Clock()
        self.fps = 60 


    def rendering(self):
        '''Main method of rendering, that render the data from players
        
        Arguments
        -----------
        coucou = la valeur'''
        pass
    

    def affichage(self,players:dict):
        self.rendering()
        self.ecran.fill(noir)
        #print(f'players number : {len(players)}')
        for player in players.values():
            for pos in player['traine']:
            #Dessine les trainées
                pygame.draw.rect(self.ecran, player['color'], pygame.Rect(pos[0], pos[1], 5, 5))
            #Dessine les motos
            self.ecran.blit(image_moto_joueur, (player['x'] - largeur_moto // 2, player['y']- hauteur_moto // 2))
        pygame.display.flip()
        self.clock.tick(self.fps)

    def close(self):
        pygame.quit()

# # Exemple d'utilisation
# if __name__ == "__main__":
#     rendering = Rendering()  # Crée une instance de la classe Rendering

#     # Exemple de joueurs fictifs

#     joueur1 = Player(100, 100, (255, 0, 0), [(100,100),(100,90),(100,80),(100,70),(100,60),(100,50),(100,40),(100,30),(100,20)])  # Joueur 1 en rouge
#     joueur2 = Player(200, 100, (0, 0, 255), [(200,100),(200,90),(200,80),(200,70),(200,60),(200,50),(200,40),(200,30),(200,20)])  # Joueur 2 en bleu
#     joueurs = {'1':joueur1, '2':joueur2}

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 rendering.close()
#                 sys.exit()

#         rendering.affichage(joueurs)
    


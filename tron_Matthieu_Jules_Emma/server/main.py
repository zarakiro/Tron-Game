from modules.network_server import NetworkServer
from modules.game import Game
import sys
import time

IP_ADDR = '172.21.72.228'
PORT = 2221
FPS = 1/10 #A changer entre 1 et par exemple 1/30 pour changer la vitesse(1 etant le plus lent)



try:
    ntw = NetworkServer(IP_ADDR, PORT)
    game = Game(ntw)
    old_time = time.time()
    while True:
        if time.time() - old_time > FPS:
            old_time = time.time()
            game.jeu()
            if game.GetVictoire():
                print("Fin du jeu !")
                ntw.close()
                sys.exit()
except KeyboardInterrupt:
    print("Interruption du clavier. Fermeture du serveur.")
finally:
    # Fermeture propre du serveur
    game.run = False
    ntw.close()
    sys.exit()







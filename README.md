# Tron-Game
# Light racer 

***Emma Molera, Jules Gueguen, Matthieu Mombert***

## But du jeu 

Light Racer est un jeu de course en 2D qui permet de piloter des motos dans toutes les directions en formant des angles droits./
**Votre objectif est simple** : battre vos adversaires en évitant de couper leur circuit, de toucher les murs et en tracant le chemin le plus rapide.

## Caractéristiques principales 

- Course de motos 
- 2 choix de vitesse
- Multijoueur en ligne pour affronter vos amis
- Nombre de partie illimité
- Incrémentation des scores
- Graphismes réalistes

## Configuration requise : 

- Système d'exploitation : Windows 10, macOS, ou Linux
- Processeur : Intel Core i5 ou plus
- Mémoire RAM : petite
- Espace de stockage disponible : très peu 

## Installation : 

1. Clonez ou téléchargez ce dépôt depuis [GitHub]
2. Assurez-vous d'avoir Python installé sur votre système
3. Installez les dépendances en exécutant `pip install -r requirements.txt` si besoin
4. Lancez le jeu en exécutant `python main.py`

## Comment jouer 

- Choisissez votre vitesse souhaitée en appuyant sur la touche 1 ou 2 
- Utilisez les touches fléchées pour contrôler la direction de votre moto
- Evitez de toucher le circuit de votre adversaire ainsi que les rebords du mur 
- Lorsqu'une personne perd, appuyer sur la touche R pour relancer une partie 
- Appuyer sur la touche ECHAP si vous voulez quitter le jeu

## Comment le jeu a été créé

### Etape 1 :  Création de la classe Player 

Cette classe représente les caractéristiques et le comportement d'un joueur dans le jeu./
La classe Player stocke des informations telles que la position du joueur, son score, etc. Elle peut également inclure des méthodes pour mettre à jour les données du joueur, gérer les mouvements et les interactions avec le jeu.

### Etape 2 : Création de la classe Network 

Cette classe est responsable de la communication réseau entre le client et le serveur du jeu. Elle peut inclure des méthodes pour établir une connexion au serveur, envoyer et recevoir des données, gérer les messages entrants, etc. /
La classe Network permet au client de s'interfacer avec le serveur de manière à envoyer des données de joueur.

### Etape 3 : Crétaion d'un fichier Client avec de nouvelles fonctions 

Il est responsable de l'interaction de l'utilisateur, de la gestion de l'interface utilisateur, de l'envoi de commandes et de données au serveur et de l'affichage des résultats sur l'écran du joueur. /
En résumé, le fichier client est la partie du jeu qui s'exécute sur l'ordinateur ou le périphérique de chaque joueur.

### Etape 4 : Crétaion d'un fichier Serveur avec de nouvelles fonctions 

Le fichier serveur contient la logique du jeu côté serveur. Il est responsable de l'hébergement du jeu, de la gestion des connexions des joueurs, de la communication avec le client. /
Le serveur garantit que le jeu se déroule de manière cohérente pour tous les joueurs en contrôlant l'état du jeu.

### Etape 4 : Crétaion d'un fichier Rendering avec de nouvelles fonctions 

Ce fichier définit une classe "Rendering" chargée de gérer l'affichage graphique du jeu en utilisant Pygame, capable de dessiner les joueurs, leurs traînées et les mettre à jour en temps réel. Il assure la création de la fenêtre de jeu, l'affichage des joueurs sous forme de rectangles colorés et l'ajout d'une image de moto pour chaque joueur, offrant ainsi une représentation visuelle du jeu.

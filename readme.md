# Projet3
Petit jeu composé d'un menu et d'un labyrinthe. On contrôle un héro qui doit récuperer des objets pour pouvoir d'échapper, s'il se présente devant le gardien sans, le joueur perd la partie.

## 1°) Prérequis.
Python3.6 et Pip sont nécessaires pour le bon fonctionnement.

## 2°) Installation.
Pour pouvoir jouer il vous faut:   
	-Télécharger le dossier du jeu.  
	-Ouvrir un terminal et aller dans le dossier du jeu.  
	-Installer les prérequis. ("pip install -r  Requirements.txt")  
	-Lancer le jeu. ("python3 main.py")  
  
## 3°) Paramétrage.
Il est possible de changer les images du personnage, du gardien ou des objets. Pour cela choisir un fichier.png de 40*40 pixels, le placer dans le dossier ressources.py et modifier le chemin correspondant dans le fichier config.py.

Représentation texte du labyrinthe :  
  'x' pour les murs  
  '  ' pour le chemin  
  'M' pour MacGyver  
  'G' pour le Gardien   

## 4°) Contrôles.
Arrivé dans le menu tappez la touche 'Entrée' pour lancer une partie.  
Pour déplacer le héro dans le labyrinthe utiliser les flèches du clavier.  
Vous pouvez quittez le jeu à tous moments en appuyant sur la touche 'Echap'.  

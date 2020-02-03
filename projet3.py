"""Fichier d'assemblage de toutes les classes."""

from screen.screen import Screen
from mapp.labyrinthe import Labyrinthe
from character.ennemy import Ennemy
from character.player import Player
from character.item import Items
from event.moteur import Moteur

LABY = Labyrinthe("mapp/map_ref.txt")
ITEM = Items(LABY.ref)
GUARD = Ennemy(LABY.ref)
MAC = Player(LABY.ref)
WIN = Screen(LABY.ref)
ENGINE = Moteur(screen=WIN, player=MAC, ennemy=GUARD, item=ITEM, mapp=LABY)

ENGINE.play()

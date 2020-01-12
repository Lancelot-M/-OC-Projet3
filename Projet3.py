#! /usr/bin/python3.6

from event.moteur import *
#import event.moteur
#from mapp import *  >>>> __all__ ?? comment ca marche

laby = Labyrinthe("mapp/map_ref.txt")
item = Items(laby.ref)
xguard = Ennemy(laby.ref)
mac = Player(laby.ref)
win = Screen(laby.ref)
engine = Moteur(screen=win, player=mac, ennemy=xguard, item=item, mapp=laby)

engine.play()

#! /usr/bin/python3.6

from position.position import Position
from event import moteur
from screen import screen
from mapp.mapper import *
from mapp.wall import *
from mapp.path import *
from character import *

laby = Mapper("mapp/map_ref.txt")
mapp = laby.ref

xwall = Wall(mapp)
xpath = Path(laby.ref)
item = Items(laby.ref)
xguard = Ennemy(laby.ref)
mac = Player(laby.ref)
win = Screen(laby.ref)
engine = Moteur(screen=win, player=mac, path=xpath, ennemy=xguard, item=item)

engine.play()

#! /usr/bin/python3.6

from getch import *
from cl_ennemy import *
from cl_labyrinthe import *
from cl_player import *
from cl_objets import *
from ft_usefile import *

f = "labytest.txt"
dico = mkdico(f)
mac = Player(dico)
gardien = Ennemy(dico)
wall = Labyrinthe("x", dico)
path = Labyrinthe([" ", "O", "G"], dico)
seringue = Objets(dico)

print("BVN DANS LE JEU TEST \n utilisez ZQSD pour vous déplacer...")
while 1:
    print(imagemap(dico))
    mac.move(path)
    if mac.pos == seringue.pos:
        mac.loot("seringue")
    if mac.pos == gardien.pos:
        mac.fight()

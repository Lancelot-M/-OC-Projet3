class Moteur:

    def __init__(self, screen=None, player=None, path=None, ennemy=None, item=None):
        self.map = "test"

    def move(self):
        if player:
            import getch
            key = getch.getch()
            new_pos = self.player.way(key) 
            if new_pos in path.pos:
                if new_pos == ennemy.pos:
                    if player.inventory == "empty":
                        screen.game_loose()
                        exit()
                    else:
                        screen.game_win()
                        exit()
                if new_pos == item.pos:
                    player.inventory = "seringue hypodermique"
                map_ref[player.pos] = " "
                player.pos = new_pos
                map_ref[pos] = "X"
        else:
            exit()

    def play(self):
        while 1:
            screen.game_map(map_ref)
            self.move()

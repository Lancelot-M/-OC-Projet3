class Player:

    def __init__(self, dico):
        self.image = 'M'
        self.gird = dico
        self.pos = self.pos = self.position()
        self.inventory = "EMPTY"

    def position(self):
        for cle, value in self.gird.items():
            if value == self.image:
                return(cle)

    def move(self, path):
        import getch
        key = getch.getch()
        if key == 'q' or key == 'Q':
            if (
                    (self.pos - 1) in path.pos
                ):
                self.pos = self.pos - 1
                self.gird[self.pos + 1] = " "
                self.gird[self.pos] = self.image
        elif key == 'z' or key == 'Z':
            if ((self.pos - 16) in path.pos):
                self.gird[self.pos] = " "
                self.pos = self.pos - 16
                self.gird[self.pos] = self.image
        elif key == 's' or key == 'S':
            if ((self.pos + 16) in path.pos):
                self.gird[self.pos] = " "
                self.pos = self.pos + 16
                self.gird[self.pos] = self.image
        elif key == 'd' or key == 'D':
            if ((self.pos + 1) in path.pos):
                self.gird[self.pos] = " "
                self.pos = self.pos + 1
                self.gird[self.pos] = self.image
        else:
            exit()

    def fight(self):
            if self.inventory == "EMPTY":
                print("Game Over")
                exit()
            else:
                print("You Win")
                exit()

    def loot(self, item):
        self.inventory = item

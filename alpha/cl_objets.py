class Objets:

    def __init__(self, dico):
        self.image = "O"
        self.gird = dico
        self.pos = self.position()

    def position(self):
        for cle, value in self.gird.items():
            if value == "O":
                return(cle)

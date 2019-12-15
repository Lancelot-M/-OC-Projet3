class Player:

    def __init__(self, dico):
        self.image = "M"
        self.pos = self.position(dico)
        self.inventory = "empty"

    def position(self, dico):
        for key, value in dico.items():
            if value == self.image:
                return key

    def way(self, way):
        if way == ('q' or 'Q'):
            return (self.pos - 1)
        elif way == ('z' or 'Z'):
            return (self.pos - 16)
        elif way == ('s' or 'S'):
            return (self.pos + 16)
        elif way == ('d' or 'D'):
            return (self.pos + 1)
        else:
            exit()

class Labyrinthe:

    def __init__(self, image, dico):
        self.image = image
        self.gird = dico
        self.pos = self.position()

    def position(self):
        l_pos = []
        for key, value in self.gird.items():
            if value in self.image:
                l_pos.append(key)
        l_pos.append(222)
        return(l_pos)

#if __name__ == '__main__':

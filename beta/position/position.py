class Position(object):

    @staticmethod
    def pos(dico):
        pos = []
        for key, value in dico.items():
            if value in self.image:
                pos.append(key)
        return pos

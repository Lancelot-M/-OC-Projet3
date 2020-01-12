class Position(object):
    @staticmethod
    def pos(dico, image="X"):
        pos = []
        for key, value in dico.items():
            if value in image:
                pos.append(key)
        return pos

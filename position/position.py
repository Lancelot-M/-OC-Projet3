class Position(object):
    """Calcul des coordonnées."""
    @staticmethod
    def pos(dico, image=""):
        pos = []
        for key, value in dico.items():
            if value in image:
                pos.append(key)
        return pos

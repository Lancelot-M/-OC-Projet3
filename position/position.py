"""File containing the function that searches for the coordinate."""


class Position(object):
    """Calculation of coordinates."""
    @staticmethod
    def pos(dico, image=""):
        """Static method."""
        pos = []
        for key, value in dico.items():
            if value in image:
                pos.append(key)
        return pos

"""Fichier contenant la fonction qui cherche la coordonnee dans le dict."""

class Position(object):
    """Calcul des coordonnees."""
    @staticmethod
    def pos(dico, image=""):
        """Methode statique."""
        pos = []
        for key, value in dico.items():
            if value in image:
                pos.append(key)
        return pos

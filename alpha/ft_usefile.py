def mkdico(file):
    c = ""
    x = 0
    dico = {}
    laby = ""
    with open(file, "r") as f:
        c = f.read(1)
        while c:
            dico[x] = c
            x += 1
            laby += c
            c = f.read(1)
        return(dico)

def imagemap(dico):
    image = ""
    for value in dico.values():
        image += value
    return(image)

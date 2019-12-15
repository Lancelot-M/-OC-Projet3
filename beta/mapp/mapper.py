class Mapper:

    def __init__(self, file_name):
        self.name = file_name
        self.ref = self.mkdico()

    def mkdico(self):
        c = ""
        x = 0
        map_ref = {}
        with open(self.name, "r") as f:
            c = f.read(1)
            while c:
                map_ref[x] = c
                x += 1
                c = f.read(1)
            return map_ref

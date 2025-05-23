class Product:
    def __init__(self, nosaukums, cena, saite):
        self.nosaukums = nosaukums
        self.cena = cena
        self.saite = saite

    def to_list(self):
        return [self.nosaukums, self.cena, self.saite]

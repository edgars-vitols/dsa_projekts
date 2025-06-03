class Product:
    def __init__(self, nosaukums: str, cena: float, saite: str, product_id: str = None):
        self.nosaukums = nosaukums
        self.cena = cena
        self.saite = saite

    def to_list(self):
        return [self.nosaukums, self.cena, self.saite]
    def __str__(self):
        return f"Nosaukums: {self.nosaukums}, Cena: {self.cena:.2f}€, Saite: {self.saite}"
    def __repr__(self):
        return f"Product(nosaukums='{self.nosaukums}', cena={self.cena}, saite='{self.saite}')"
    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.nosaukums == other.nosaukums and self.cena == other.cena and self.saite == other.saite
    def __hash__(self):
        return hash((self.nosaukums, self.cena, self.saite))
     @property
    def hash_value(self):
        if self._hash_value is None:
        return self._hash_value

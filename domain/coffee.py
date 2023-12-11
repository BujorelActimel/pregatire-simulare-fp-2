class Coffee:
    def __init__(self, name, country, price):
        self._name = name
        self._country = country
        self._price = price

    def __str__(self):
        return f"{self.name} from {self.country}: {self.price}$"

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self._name
    
    @property
    def country(self):
        return self._country
    
    @property
    def price(self):
        return self._price

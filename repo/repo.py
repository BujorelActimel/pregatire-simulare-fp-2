from domain import Coffee

class Repo:
    def __init__(self, file_name):
        self._file_name = file_name
        self._coffee_list = self.loadData()

    @property
    def coffee_list(self):
        return self._coffee_list

    @property
    def file_name(self):
        return self._file_name

    def add_coffee(self, name, country, price):
        for coffee in self.coffee_list:
            if coffee.name == name:
                raise ValueError("Coffee name already exists")

        self.coffee_list.append(Coffee(name, country, price))
    
    def loadData(self):
        coffee_list = []

        with open(self.file_name, "r") as f:
            coffees = f.readlines()
        
        for coffee in coffees[1:]:
            name, country, price = coffee.strip().split(",")
            price = float(price)
            coffee_list.append(Coffee(name, country, price))
        
        return coffee_list

    def saveData(self):
        with open(self.file_name, "w") as f:
            f.write("nume,tara,pret\n")
            for coffee in self.coffee_list:
                f.write(f"{coffee.name},{coffee.country},{coffee.price}\n")

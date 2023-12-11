class Service:
    def __init__(self, repo):
        self._repo = repo

    @property
    def repo(self):
        return self._repo

    def sortByCountryAndPrice(self):
        return sorted(self.repo.coffee_list, key=lambda x: (x.country.lower(), x.price))
    
    def filterByCountryAndPrice(self, country, price):
        if country == "" and price == "":
            raise ValueError("Introduceti tara si/sau pretul")
        
        elif country == "":
            try:
                price = float(price)
            except ValueError:
                raise ValueError("Pret gresit")
            else:
                filtered = filter(lambda x: x.price <= price, self.repo.coffee_list)
        
        elif price == "":
            filtered = filter(lambda x: x.country == country, self.repo.coffee_list)

        else:
            try:
                price = float(price)
            except ValueError:
                raise ValueError("Pret gresit")
            else:
                filtered = filter(lambda x: x.country == country and x.price <= price, self.repo.coffee_list)
        

        filtered_list = list(filtered)
        if filtered_list:
            return filtered_list
        else:
            raise ValueError("Nu s-a gasit nicio cafea cu specificatiile dorite")

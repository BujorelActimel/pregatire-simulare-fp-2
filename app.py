import os
from utils import Utility
from domain import Coffee
from repo import Repo
from service import Service

class App:
    def __init__(self):
        self._utils = Utility()
        self._repo = Repo("data/coffees.csv")
        self._service = Service(self.repo)

    @property
    def utils(self):
        return self._utils

    @property
    def repo(self):
        return self._repo

    @property
    def service(self):
        return self._service

    def menu(self):
        os.system("cls")
        print("""Choose an option:
        1. Add a Coffee
        2. Display All Coffees
        3. Filter Coffees
        4. Exit
        """)

    def run(self):
        while True:
            self.menu()
            option = self.utils.get_command()

            if option == 1:
                name = self.utils.get_text_input("Coffee Name: ")
                country = self.utils.get_text_input("Country of Origin: ")
                price = self.utils.get_numerical_input("Price: ")

                try:
                    self.repo.add_coffee(name, country, price)
                except ValueError as error:
                    self.utils.enter(error)
                else:
                    self.utils.enter(self.repo.coffee_list)
                
            if option == 2:
                self.utils.enter(self.service.sortByCountryAndPrice())

            if option == 3:
                country = self.utils.get_text_input("Country: ")
                price = self.utils.get_text_input("Price: ")
                try:
                    self.utils.enter(self.service.filterByCountryAndPrice(country, price))
                except ValueError as error:
                    self.utils.enter(error)

            if option == 4:
                self.repo.saveData()
                break


if __name__ == "__main__":
    app = App()
    app.run()

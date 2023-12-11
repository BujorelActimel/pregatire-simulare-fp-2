from domain import Coffee
from repo import Repo

def test_coffee_name():
    repo = Repo("domain/test_coffee.csv")
    repo.add_coffee("Brazil", "Brazil", 10)
    coffee = repo.coffee_list[0]
    assert coffee.name == "Brazil"

    try:
        repo.add_coffee("Brazil", "Brazil", 10)
        assert False
    except ValueError:
        assert True

def test_coffee_country():
    coffee = Coffee("Brazil", "Brazil", 10)
    assert coffee.country == "Brazil"

def test_coffee_price():
    coffee = Coffee("Brazil", "Brazil", 10)
    assert coffee.price == 10

def test_coffee_str():
    coffee = Coffee("Brazil", "Brazil", 10)
    assert str(coffee) == "Brazil from Brazil: 10$"

def test_coffee_repr():
    coffee = Coffee("Brazil", "Brazil", 10)
    assert repr(coffee) == "Brazil from Brazil: 10$"

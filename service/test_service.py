from service import Service
from repo import Repo

def test_service():
    repo = Repo("service/test_service.csv")
    service = Service(repo)
    assert service.repo.file_name == "service/test_service.csv"
    assert len(service.repo.coffee_list) == 4

def test_sortByCountryAndPrice():
    repo = Repo("service/test_service.csv")
    service = Service(repo)
    assert service.sortByCountryAndPrice() == [repo.coffee_list[3], repo.coffee_list[2], repo.coffee_list[1], repo.coffee_list[0]]

def test_filterByCountryAndPrice():
    repo = Repo("service/test_service.csv")
    service = Service(repo)
    assert service.filterByCountryAndPrice("Brazil", "9") == [repo.coffee_list[3]]
    assert service.filterByCountryAndPrice("Brazil", "") == [repo.coffee_list[2], repo.coffee_list[3]]
    assert service.filterByCountryAndPrice("", "9") == [repo.coffee_list[3]]
    try:
        service.filterByCountryAndPrice("", "")
        assert False
    except ValueError:
        assert True

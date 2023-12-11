from repo import Repo

def test_repo_init():
    repo = Repo("repo/test_repo.csv")
    assert repo.file_name == "repo/test_repo.csv"
    assert len(repo.coffee_list) == 3
    assert repo.coffee_list[0].name == "Brazil"
    assert repo.coffee_list[0].country == "Brazil"
    assert repo.coffee_list[0].price == 10
    assert repo.coffee_list[1].name == "Colombia"
    assert repo.coffee_list[1].country == "Colombia"
    assert repo.coffee_list[1].price == 20
    assert repo.coffee_list[2].name == "Ethiopia"
    assert repo.coffee_list[2].country == "Ethiopia"
    assert repo.coffee_list[2].price == 30

def test_repo_add_coffee():
    repo = Repo("repo/test_repo.csv")
    repo.add_coffee("Arabica", "Arabica", 10)
    assert len(repo.coffee_list) == 4
    assert repo.coffee_list[3].name == "Arabica"
    assert repo.coffee_list[3].country == "Arabica"
    assert repo.coffee_list[3].price == 10

    try:
        repo.add_coffee("Brazil", "Brazil", 10)
        assert False
    except ValueError:
        assert True

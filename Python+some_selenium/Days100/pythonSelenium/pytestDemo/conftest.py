import pytest

@pytest.fixture()#scope="class")
def setup():
    print("I will be executed first.")
    yield
    print("I'll be executed last.")


@pytest.fixture()
def data_load():
    print("User profile is beeng created.")
    return ["Name", "Surename", "namesurname.com"]


@pytest.fixture(params=[("chrome", "Rahul", "shetty"), ("Firefox", "shetty"), ("IE", "SS")])
def crossBrowser(request):
    return request.param




import pytest


# @pytest.fixture()
# def setup():
#     print("I will be executed first.")
#     yield
#     print("I'll be executed last.")

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixture_demo(self):
        print("Executed after fixture if you passes the name of fixture as a test parameter. \
        Test parameter is send automatically when using @pytest.mark.usefixtures('setup')")

    def test_fixture_demo1(self):
        print("Executed after fixture_demo1 if you passes the name of fixture as a test parameter. \
        Test parameter is send automatically when using @pytest.mark.usefixtures('setup')")

    def test_fixture_demo2(self):
        print("Executed after fixture_demo2 if you passes the name of fixture as a test parameter. \
        Test parameter is send automatically when using @pytest.mark.usefixtures('setup')")

    def test_fixture_demo3(self):
        print("Executed after fixture_demo3 if you passes the name of fixture as a test parameter. \
        Test parameter is send automatically when using @pytest.mark.usefixtures('setup')")



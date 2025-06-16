# Any pytest file should start with test_<file_name> or end with <file_name>_test
# Any pytest method names should start with test_<test_name>
# Any code should be wrapped into the methods
# method names have sense
# -k -> stands for the method name execution(checking by method name)
# -s -> outputs logs, e.g. print() in terminal
# -v -> more metadata informations are present in logs
#  can can run specific file with: py.test <file_name> -k text -s -v
# you can skip test with: @pytest.mark.skip
# you can run the tests but without reporting it status, e.g.
# when failing but bug is reported and not fixed yet
# but you need the performed operations or data from that failing test: @pytest.mark.xfail
# fixtures are used as a setup and tear down for test cases
# conftest.py file -> to generalized fixtures and make it available for the whole test_cases\files
# use class to apply fixtures to all wrapped test cases
# if you need to execute only once fixture you can use in conftest.py option: scope="class"
# datadriven and parametrization can be done with return format in the list format
#
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    msg = "Hello"
    assert msg == "Hi", "Test fail because string are different."


@pytest.mark.unit
def test_second_credit_card():
    a = 4
    b = 6
    assert a + b == 6, "Addition do not match."


# @pytest.fixture()
# def setup():
#     print("I will be executed first")


def test_fixture_demo(setup):
    print("Executed after fixture if you passes the name of fixture as a test parameter.")


# Any pytest file should start with test_<file_name> or end with <file_name>_test
# Any pytest method names should start with test_<test_name>
# Any code should be wrapped into the methods
# You can mark with tag: @pytest.mark.smoke and then run with -m <mark_name> option
import pytest


@pytest.mark.smoke
def test_first_program():
    print("\nHello")

@pytest.mark.unit
@pytest.mark.xfail
def test_second_greet_credit_card():
    print("\nGood Morning!")


def test_cross_browser(crossBrowser):
    print(crossBrowser)

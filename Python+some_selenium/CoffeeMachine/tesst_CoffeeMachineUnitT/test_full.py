import pytest

from MyCoffeeMachine import CMParameters
from MyCoffeeMachine.MakeACoffie import MakeACoffee

mk = MakeACoffee(CMParameters.machine_parameters, CMParameters.coffee_options, CMParameters.type_of_coins)


def test_user_choice():
    for choice in ["espresso", "latte", "cappuccino", "report", "abc", "12354", "off"]:
        mk1 = MakeACoffee(CMParameters.machine_parameters, CMParameters.coffee_options, CMParameters.type_of_coins)
        u_choice = mk1.user_choice(choice)
        assert u_choice in ["espreso", "latte", "cappuccino", "report", "off"], "User choice method fails."
        if choice in ["abc", "12354"]:
            assert u_choice is None, "Returned unexpected value"


def test_insert_coins_feature():
    mk.insert_coins()

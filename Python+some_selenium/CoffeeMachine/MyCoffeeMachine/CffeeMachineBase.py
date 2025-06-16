class CoffeeMachine:

    def __init__(self, machine_parameters, coffee_options, type_of_coins):
        self.mp = machine_parameters
        self.coffee = coffee_options
        self.user_choice = ""
        self.coins = type_of_coins
        self.inserted_coins_amount = {
                                "quarters": 0,
                                "dimes": 0,
                                "nickles": 0,
                                "pennies": 0
                            }

    def __del__(self):
        print("Turning OFF.")

    def report(self):
        print(f"Water: {self.mp['water']}")
        print(f"Milk: {self.mp['milk']}")
        print(f"Coffee: {self.mp['coffee']}")
        print(f"Money: {self.mp['money']}")



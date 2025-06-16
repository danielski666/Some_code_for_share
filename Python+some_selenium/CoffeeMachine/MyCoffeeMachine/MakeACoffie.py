from MyCoffeeMachine.CffeeMachineBase import CoffeeMachine


class MakeACoffee(CoffeeMachine):

    def ask_user(self):
        self.user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if self.user_choice == "off":
            return "off"
        elif self.user_choice == "espresso":
            print(f"Espresso cost: {round(self.coffee[self.user_choice]['cost'], 2)}")
            return self.user_choice
        elif self.user_choice == "latte":
            print(f"Latte cost: {round(self.coffee[self.user_choice]['cost'], 2)}")
            return self.user_choice
        elif self.user_choice == "cappuccino":
            print(f"Cappuccino cost: {round(self.coffee[self.user_choice]['cost'], 2)}")
            return self.user_choice
        elif self.user_choice == "report":
            self.report()
            return "report"

    def insert_coins(self):
        print("Insert coins: ")
        self.inserted_coins_amount["quarters"] = int(input("quarters: "))
        self.inserted_coins_amount["dimes"] = int(input("dimes: "))
        self.inserted_coins_amount["nickles"] = int(input("nickles: "))
        self.inserted_coins_amount["pennies"] = int(input("pennies: "))

    def transaction_success(self, option):
        sum_of_coins = self.coins["quarters"] * self.inserted_coins_amount["quarters"] + \
                       self.coins["dimes"] * self.inserted_coins_amount["dimes"] + \
                       self.coins["nickles"] * self.inserted_coins_amount["nickles"] + \
                       self.coins["pennies"] * self.inserted_coins_amount["pennies"]

        if round(sum_of_coins, 2) < self.coffee[option]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        elif round(sum_of_coins, 2) == self.coffee[option]["cost"]:
            self.mp['money'] += self.coffee[option]["cost"]
            self.make_a_coffe(self.coffee[option]["water"], self.coffee[option]["milk"], self.coffee[option]["coffee"])
            print(f"Here is your {option}. Enjoy!")
            self.user_choice = ""
        else:
            self.mp['money'] += self.coffee[option]["cost"]
            self.make_a_coffe(self.coffee[option]["water"], self.coffee[option]["milk"], self.coffee[option]["coffee"])
            print(f"Here is ${round((sum_of_coins - self.coffee[option]['cost']), 2)} dollars in change.")
            print(f"Here is your {option} ☕. Enjoy!")
            self.user_choice = ""

    def check_resources(self):
        if self.mp['water'] < self.coffee[self.user_choice]["water"]:
            print("Sorry there is not enough water.")
            return False
        elif self.mp['milk'] < self.coffee[self.user_choice]["milk"]:
            print("Sorry there is not enough milk.")
            return False
        elif self.mp['coffee'] < self.coffee[self.user_choice]["coffee"]:
            print("Sorry there is not enough coffee beans.")
            return False

    def make_a_coffe(self, water, milk, coffee):
        self.mp['water'] -= water
        self.mp['milk'] -= milk
        self.mp['coffee'] -= coffee

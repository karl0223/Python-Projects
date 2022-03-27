MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def coffee_ingredients_water(coffee):
    water = MENU[coffee]["ingredients"]["water"]
    return water


def coffee_ingredients_coffee(coffee):
    coffee = MENU[coffee]["ingredients"]["coffee"]
    return coffee


def coffee_ingredients_milk(coffee):
    milk = MENU[coffee]["ingredients"]["milk"]
    return milk


def coffee_cost(coffee):
    coffee = MENU[coffee]["cost"]
    return coffee


def get_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")


def get_resources_water():
    water = resources["water"]
    return water


def get_resources_milk():
    milk = resources["milk"]
    return milk


def get_resources_coffee():
    coffee = resources["coffee"]
    return coffee


def process_coins():
    print("Please insert coins.")
    quarter_coin = int(input("How many quarters? : "))
    dimes_coin = int(input("How many dimes? : "))
    nickles_coin = int(input("How many nickles? : "))
    pennies_coin = int(input("How many pennies? : "))

    total = quarter_coin * QUARTER + dimes_coin * DIME + nickles_coin * NICKLE + pennies_coin * PENNIES

    return total


def is_sufficient(coffee):
    if get_resources_water() >= coffee_ingredients_water(coffee):
        if get_resources_coffee() >= coffee_ingredients_coffee(coffee):
            if coffee == "espresso":
                return True
            elif get_resources_milk() >= coffee_ingredients_milk(coffee):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

# def is_resource_sufficient(order_ingredients):
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}.")
#             return False
#     return True



def refill():
    resources["water"] += 300
    resources["coffee"] += 100
    resources["milk"] += 200


QUARTER = 0.25
DIME = 0.1
NICKLE = 0.05
PENNIES = 0.01

should_continue = True
while should_continue:
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        get_resources()
    elif user_input == "off":
        should_continue = False
    elif user_input == "refill":
        refill()
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        if is_sufficient(user_input):
            payment = process_coins()
            cost = coffee_cost(user_input)

            if payment > cost:
                water_level = get_resources_water() - coffee_ingredients_water(user_input)
                coffee_amount = get_resources_coffee() - coffee_ingredients_coffee(user_input)
                if user_input != "espresso":
                    milk_level = get_resources_milk() - coffee_ingredients_milk(user_input)
                else:
                    milk_level = resources["milk"]

                resources["water"] = water_level
                resources["coffee"] = coffee_amount
                resources["milk"] = milk_level
                resources["money"] = cost

                change = round(payment - cost, 2)

                print(f"Here is ${change} in change.")
                print(f"Here is your {user_input} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry there is not enough ingredients.")



# TODO 1: Prompt user by asking “​What would you like? (espresso/latte/cappuccino):​ check
# TODO 2: Turn off the Coffee Machine by entering “​off​ ” to the prompt.
# TODO 3: Print report. check
# TODO 4: Check resources sufficient?
# TODO 5: Process coins.
# TODO 6: Check transaction successful?
# TODO 7: Make Coffee.

# TODO: Solution

# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True
#
#
# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total
#
#
# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False
#
#
# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")
#
#
# is_on = True
#
# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])

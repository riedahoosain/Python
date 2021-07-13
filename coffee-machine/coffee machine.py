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

PENNIES = 0.01
NICKELS = 0.05
DIMES = 0.10
QUARTERS = 0.25
profit = 0.00
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_available_resources(water, milk, coffee):
    if resources["water"] > water:
        if resources["milk"] > milk:
            if resources["coffee"] > coffee:
                return True
    else:
        return False

    # if resources["water"] > water and resources["milk"] > milk and resources[coffee] > coffee:
    #     return "There is enough resources to make this"
    # else:
    #     return "Not enough resources are available"


def accept_currency(cost_coffee):
    total_quarters = float(input("How many quarters?: ")) * QUARTERS
    total_dimes = float(input("How many dimes?: ")) * DIMES
    total_nickels = float(input("How many nickels?: ")) * NICKELS
    total_pennies = float(input("How many pennies?")) * PENNIES

    amount_given = total_quarters + total_dimes + total_nickels + total_pennies
    print(amount_given)
    if amount_given >= cost_coffee:
        print(f"Here is ${amount_given - cost_coffee} in Change")
        print("Here is your hot drink")
    else:
        print("You don't have enough")


# TODO: 3. Print available resources
def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit}")


def coffee_program():
    machine_on = True
    while machine_on:

        user_choice = input(
            "What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            machine_on = False

        elif user_choice == "report":
            print_report()

        elif user_choice == "espresso":
            name = MENU[user_choice]
            water_needed = (name["ingredients"]["water"])
            milk_needed = 0
            coffee_needed = (name["ingredients"]["coffee"])
            enough_resources = check_available_resources(
                water_needed, milk_needed, coffee_needed)
            if enough_resources:
                coffee_cost = (name["cost"])
                accept_currency(coffee_cost)
                global profit
                profit += coffee_cost
                resources["water"] -= water_needed
                resources["coffee"] -= coffee_needed
            else:
                print("We are out of ingredients")

        elif user_choice == "latte" or user_choice == "cappuccino":
            name = MENU[user_choice]
            water_needed = (name["ingredients"]["water"])
            milk_needed = (name["ingredients"]["milk"])
            coffee_needed = (name["ingredients"]["coffee"])
            enough_resources = check_available_resources(
                water_needed, milk_needed, coffee_needed)
            if enough_resources:
                coffee_cost = (name["cost"])
                print(coffee_cost)
                accept_currency(coffee_cost)
                # global profit
                profit += coffee_cost
                resources["water"] -= water_needed
                resources["milk"] -= milk_needed
                resources["coffee"] -= coffee_needed
            else:
                print("We are out of ingredients")

        else:
            print("You have not made a valid selection")


coffee_program()

# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

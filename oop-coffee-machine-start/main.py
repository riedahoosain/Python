from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Show menu & ask user to choose an item
# TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino/): ”
is_machine_on = True
while is_machine_on:

    menu_items = coffee_menu.get_items()
    user_choice = input(f"What would you like? ({menu_items}): ")

# TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_choice == "off":
        print("Turning the machine off")
        is_machine_on = False

# TODO 3. Print report.
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = coffee_menu.find_drink(user_choice)
        is_there_enough_ingredients = coffee_maker.is_resource_sufficient(
            drink)
        is_payment_successful = money_machine.make_payment(drink.cost)
        if is_there_enough_ingredients:
            if is_payment_successful:
                coffee_maker.make_coffee(drink)

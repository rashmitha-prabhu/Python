from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    choice = input(f"What would you like? ({menu.get_items()})  : ")

    if choice.lower() == 'off':
        is_on = False
        print("Shutting Down")

    elif choice.lower() == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice.lower())
        if drink is None:
            continue
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

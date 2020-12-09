import art

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
}


def check_resources(beverage):
    for ingredient in beverage['ingredients']:
        if resources[ingredient] < beverage['ingredients'][ingredient]:
            print(f"Sorry. I'm running low on {ingredient} :(")
            return False
    return True


def coins():
    quarters = int(input("Quarters : "))
    dimes = int(input("Dimes : "))
    nickles = int(input("Nickles : "))
    pennies = int(input("Pennies : "))
    money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    return money


def update_resources(beverage):
    for ingredient in beverage['ingredients']:
        resources[ingredient] -= beverage['ingredients'][ingredient]


profit = 0
is_on = True

print(art.logo)

while is_on:
    print("\nWhat would you like today ?")
    choice = input("Espresso / Latte / Cappuccino\t: ").lower()
    if choice == 'off':
        is_on = False

    elif choice == 'report':
        print(f"\n\tWater : {resources['water']}")
        print(f"\tMilk : {resources['milk']}")
        print(f"\tCoffee : {resources['coffee']}")
        print(f"\tMoney : ${profit:.2f}")

    else:
        drink = MENU[choice]
        if check_resources(drink):
            print(f"Your drink costs ${drink['cost']:.2f}")
            print("Insert coins : ")
            amount = coins()
            if amount >= drink['cost']:
                change = amount - drink['cost']
                if change > 0:
                    print(f"You paid ${amount:.2f}. Here's ${change:.2f} in change")
                print("Brewing...")
                update_resources(drink)
                profit += drink['cost']
                print(f"Here's your {choice.title()}. Enjoy :)")
            else:
                print("Sorry, That's not enough money.\nMoney refunded")

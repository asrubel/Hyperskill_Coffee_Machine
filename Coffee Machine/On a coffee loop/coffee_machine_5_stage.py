water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def remaining():
    global water, milk, coffee_beans, disposable_cups, money
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"${money} of money")


def make_action(action_to_make):
    if action_to_make == 'buy':
        buy()
    elif action_to_make == 'fill':
        fill()
    elif action_to_make == 'take':
        take()
    elif action_to_make == 'remaining':
        remaining()


def buy():
    global water, milk, coffee_beans, disposable_cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    kind = input()
    if kind == '1':
        make_coffee(water_req=250, milk_req=0, coffee_req=16, cost=4)
    if kind == '2':
        make_coffee(water_req=350, milk_req=75, coffee_req=20, cost=7)
    if kind == '3':
        make_coffee(water_req=200, milk_req=100, coffee_req=12, cost=6)


def make_coffee(water_req, milk_req, coffee_req, cost):
    global water, milk, coffee_beans, disposable_cups, money
    if water - water_req < 0:
        print("Sorry, not enough water!")
    elif milk - milk_req < 0:
        print("Sorry, not enough milk!")
    elif coffee_beans - coffee_req < 0:
        print("Sorry, not enough coffee beans!")
    elif disposable_cups - 1 < 0:
        print("Sorry, not enough disposable cups!")
    else:
        water -= water_req
        milk -= milk_req
        coffee_beans -= coffee_req
        money += cost
        disposable_cups -= 1
        print("I have enough resources, making you a coffee!")


def fill():
    global water, milk, coffee_beans, disposable_cups, money
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups do you want to add:")
    disposable_cups += int(input())


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == 'exit':
        break
    make_action(action)

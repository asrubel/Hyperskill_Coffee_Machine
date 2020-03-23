water = 1200
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
    print(f"{money} of money")


def buy():
    global water, milk, coffee_beans, disposable_cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    kind = int(input())
    if kind in [1, 2, 3]:
        disposable_cups -= 1
        if kind == 1:
            water -= 250
            coffee_beans -= 16
            money += 4
        elif kind == 2:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
        elif kind == 3:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6


def fill():
    global water, milk, coffee_beans, disposable_cups
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups += int(input())


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


def make_action():
    print("Write action (buy, fill, take):")
    action = input()
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    remaining()


remaining()
make_action()

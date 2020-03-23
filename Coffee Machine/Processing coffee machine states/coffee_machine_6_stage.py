# Write your code here
class CoffeeMachine:

    def __init__(self, water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money
        self.state = 'ready'

    def remaining(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"{self.money} of money")

    def buy(self, action):
        if action in ['1', '2', '3', 'back']:
            if action == '1':
                self.make_coffee(water_req=250, milk_req=0, coffee_req=16, cost=4)
            elif action == '2':
                self.make_coffee(water_req=350, milk_req=75, coffee_req=20, cost=7)
            elif action == '3':
                self.make_coffee(water_req=200, milk_req=100, coffee_req=12, cost=6)
            elif action == 'back':
                pass
        else:
            pass

    def make_coffee(self, water_req, milk_req, coffee_req, cost):
        if self.water - water_req < 0:
            print("Sorry, not enough water!")
        elif self.milk - milk_req < 0:
            print("Sorry, not enough milk!")
        elif self.coffee_beans - coffee_req < 0:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups - 1 < 0:
            print("Sorry, not enough disposable cups!")
        else:
            self.water -= water_req
            self.milk -= milk_req
            self.coffee_beans -= coffee_req
            self.money += cost
            self.disposable_cups -= 1
            print("I have enough resources, making you a coffee!")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.coffee_beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def make_action(self, action):
        if self.state == 'ready':
            if action == 'buy':
                self.state = 'buying'
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                self.state = 'turned_off'
        elif self.state == 'buying':
            self.buy(action)
            self.state = 'ready'


coffee_machine = CoffeeMachine()
while True:
    action_to_make = input()
    coffee_machine.make_action(action_to_make)
    if coffee_machine.state == 'turned_off':
        break

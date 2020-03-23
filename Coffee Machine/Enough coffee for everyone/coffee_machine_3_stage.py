# Write your code here
water_per_cup = 200
milk_per_cup = 50
coffee_per_cup = 15

print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee_beans = int(input())
print("Write how many cups of coffee you will need:")
cups = int(input())

possible_cups_by_water = water // water_per_cup
possible_cups_by_milk = milk // milk_per_cup
possible_cups_by_coffee = coffee_beans // coffee_per_cup
possible_cups = min(possible_cups_by_water, possible_cups_by_milk, possible_cups_by_coffee)

if cups == possible_cups:
    print("Yes, I can make that amount of coffee")
elif cups < possible_cups:
    print("Yes, I can make that amount of coffee (and even {} more than that)"
          .format(possible_cups - cups))
else:
    print("No, I can make only {} cups of coffee".format(possible_cups))
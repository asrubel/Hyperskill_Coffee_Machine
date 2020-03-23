# Write your code here
water_per_cup = 200
milk_per_cup = 50
coffee_beans = 15

cups = int(input("Write how many cups of coffee you will need:"))
print("For {} cups of coffee you will need:".format(cups))
print("{} ml of water".format(water_per_cup * cups))
print("{} ml of milk".format(milk_per_cup * cups))
print("{} g of coffee beans".format(coffee_beans * cups))
'''
quarter = 4
dime = 3
nickel = 2
penny = 1

'''
'''
quarter = input("Enter number of quarters: ")
dime = input("Enter number of dimes: ")
nickel = input("Enter number of nickels: ")
penny = input("Enter number of pennies: ")
'''
'''
quarter = int(input())
dime = int(input())
nickel = int(input())
penny = int(input())

quarter *= .25
dime *= .10
nickel *= .05
penny *= .01

dollars = quarter + dime + nickel + penny
print(f"Amount: ${dollars:.2f}")
'''
'''
quarter = int(input()) * .25
dime = int(input()) * .10
nickel = int(input()) * .05
penny = int(input()) * .01

dollars = quarter + dime + nickel + penny

print(f"Amount: ${dollars:.2f}")
'''
import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

wall_height = int(input('Enter wall height (feet):\n'))
# Calculate and output wall area
wall_width = int(input('Enter wall width (feet):\n'))
area = wall_height * wall_width
gallon = area/350
cans = math.ceil(gallon)


print('Wall area:', area, "square feet")
print("Paint needed:",'{:.2f}'.format(gallon), "gallons")
print("Cans needed:", cans, "can(s)")

color_choice = input("\nChoose a color to paint the wall:\n")

if color_choice in paint_colors:
    print("Cost of purchasing", color_choice,"paint: " + "$" + str(paint_colors[color_choice] * cans))
else:
    print("Invalid paint color")


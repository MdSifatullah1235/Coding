units = float(input("Enter the amount of units consumed: "))

if units < 50:
    unit_cost = units * 2.60
    tax = 25

elif units <= 100:
    unit_cost = 130 + ((units - 50) * 3.25)
    tax = 35

elif units <= 200:
    unit_cost = 130 + 162.50 + ((units - 100) * 5.26)
    tax = 45

else:
    unit_cost = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    tax = 75

total = unit_cost + tax

print("The total electrical bill is: %.2f" %total)
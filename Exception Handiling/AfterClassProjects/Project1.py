try:
    num1 = int(input("Enter Your Age: "))

except ValueError:
    print("Wrong Value")

except:
    print("Wrong Input")

else:
    print("All Ok")
    valid = False
    while not valid:
        if num1 % 2 == 0:
            print("This Number Is An Even Number!")
            valid = True
        elif num1 % 3 == 0:
            print("This Number Is An Odd Number!")
            valid = True

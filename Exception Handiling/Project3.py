valid = False
try:
    x = int(input("Enter a Number :"))
    while not valid:
        if x % 2 == 0:
            print("bye")
        valid = True
except ValueError:
    print("Invalid")
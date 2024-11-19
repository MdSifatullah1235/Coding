a = int(input("Enter a number for the value (a): "))
b = int(input("Enter a number for the value (b): "))
c = int(input("Enter a number for the value (c): "))

if a == b and a == c:
    print("a, b, and c are equal")

elif a == b and a > c:
    print("a and b are equal, but c is lower")

elif a == b and a < c:
    print("a and b are equal, but c is greater")

elif b == c and b > a:
    print("b and c are equal, but a is lower")

elif b == c and b < a:
    print("b and c are equal, but a is greater")

elif a == c and a > b:
    print("a and c are equal, but b is lower")

elif a == c and a < b:
    print("a and c are equal, but b is greater")

else:
    if a > b and a > c:
        print("a is greater than b and c")

    elif b > a and b > c:
        print("b is greater than a and c")

    elif c > a and c > b:
        print("c is greater than a and b")
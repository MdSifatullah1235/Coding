def add(num1, num2):
    sum = num1 + num2
    return sum

def subtract(num1, num2):
    difference = num1 - num2
    return difference

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(num1, num2):
        quotient = num1 / num2
        return quotient

print("Enter an operation")

print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = input("Choose an operation: ")
nnum1 = float(input("Enter the first number: "))
nnum2 = float(input("Enter the second number: "))

if choice == "a":
    res = add(nnum1, nnum2)
    print("The result is " , add(nnum1, nnum2))
elif choice == "b":
    res = subtract(nnum1, nnum2)
    print("The result is " , subtract(nnum1, nnum2))
elif choice == "c":
    res = multiply(nnum1, nnum2)
    print("The result is " , multiply(nnum1, nnum2))
elif choice == "d":
    res = divide(nnum1, nnum2)
    print("The result is " , divide(nnum1, nnum2))
else:
    print("Invalid choice. Please choose a valid operation.")
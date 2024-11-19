base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result = 1 

for i in range(1, exponent + 1):
    result *= base
    print("Power {}: {}^{} = {}".format(i, base, i, result))

print("Final result: {}^{} = {}".format(base, exponent, result))
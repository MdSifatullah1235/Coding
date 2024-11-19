print("Enter a amount of (*)")
n = int(input("Enter a amount :"))

for i in range(n):
    for j in range(i + 1):
        print("* " , end="")
    print()
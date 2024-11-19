num_input = int(input("Enter a number :"))

num = num_input % 10


if (num % 6 == 0):
    print(num_input , "is divisible by 3 and 2")


else:
    print(num_input , "is not divisible by 3 and 2")
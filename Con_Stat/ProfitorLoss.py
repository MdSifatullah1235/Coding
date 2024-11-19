cost = float(input("Enter the actual product price : "))
sale = float(input("Enter the sale amount : "))

if (sale > cost):
    amount_1 = sale - cost
    print("The profit is {} ".format(amount_1))

else:
    amount_2 = cost - sale
    print("The loss is {} ".format(amount_2))
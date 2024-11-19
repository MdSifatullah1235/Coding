try:
    num1, num2 = eval(input("Enter Two Numbers With a Comma Betwen The Numbers : "))
    res = num1 / num2
    print("The Result is", res)

except ZeroDivisionError:
    print("There Should Be No Zeros")

except SyntaxError :
    print("A Comma is Missing")

except:
    print("Wrong Input")

else:
    print("All ok")

finally:
    print("This will execute no matter what")
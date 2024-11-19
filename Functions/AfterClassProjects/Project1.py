def function(r):
    circumference = 2 * 3.14159 * r
    return circumference

innum1 = float(input("Enter the radius: "))
res = function(innum1)
print("The result is: {:.2f}".format(res))
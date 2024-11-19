num = int(input("Enter a number: "))
count = 0
temp = num

while temp > 0:
    temp //= 10  
    count += 1
    
print("The number of digits in {} is {}".format(num,count))
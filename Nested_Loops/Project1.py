string = input("Enter your word :")
char = input("Enter the chracter you want to know has occured in the word :")

i = 0
count = 0

while i < len(string):
    if string[i] == char:
        count += 1

    i += 1
print("The number of times {} has occured is {}".format(char,count))  
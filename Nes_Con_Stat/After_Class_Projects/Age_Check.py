inp = int(input("Enter your age: "))

if inp <= 0:
    print("Stop Joking")
elif inp >= 10:
    if inp > 20:
        print("You're older than 20, you cannot enter")
        if inp >= 40:
            print("Also, you're very old")

    else:
        print("You can enter")

else:
    print("You're younger than 10, you cannot enter")
    
    if inp <= 5:
        print("Also, you are a little kid")
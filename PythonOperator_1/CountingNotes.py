amount_input = int(input("Enter an amount within the multiplication of 100, 50 or 10 taka to withdraw: "))
print(amount_input)

note1 = amount_input // 100
note2 = (amount_input % 100) // 50
note3 = ((amount_input % 100) % 50) // 10

print("The amount of 100 taka notes:", int(note1))
print("The amount of 50 taka notes:", int(note2))
print("The amount of 10 taka notes:", int(note3))
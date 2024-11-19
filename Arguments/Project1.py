def total_calc(bill,tip_per):
    total = bill*(1 + 0.01 * tip_per)
    total = round(total,2)
    print(f"Please pay ${total}")

total_calc(150,20)
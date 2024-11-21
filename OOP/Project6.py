class Pair_Elements():
    def __init__(self, nums , target):
        store = {}
        for i, num in enumerate(nums):
            if target - num in store:
                return (target - num,num)
            store[num] = i

nums = (10,20,30,40,50,60,70,80,90)

value = int(input("Enter the elements :"))

print(Pair_Elements().sum(nums, value ))
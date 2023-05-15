from collections import Counter

def sirala(nums):
    variable = nums[0]
    unique = []
    piece = 1

    for i in range(len(nums)):
        if i == 0:
            unique.append(nums[i])
        if nums[i] != variable:
            piece += 1
            variable = nums[i]
            unique.append(variable)

    return unique

print(sirala([1,1,2]))
"""
from collections import Counter

def sirala(nums):
    num = Counter(nums)
    piece = []

    for i in range(len(num.keys())):
        print(num.keys([i]))

    return piece

print(sirala([0,0,1,1,1,2,2,3,3,4]))
"""
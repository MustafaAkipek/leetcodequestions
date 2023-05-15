from collections import Counter

def sirala(nums):
    variable = nums[0]
    unique = [variable]
    piece = 1

    for i in range(len(nums)):
        if nums[i] != variable:
            piece += 1
            variable = nums[i]
            unique.append(variable)

    return unique

print(sirala([0,0,0,1,2,2,2,3,4]))
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
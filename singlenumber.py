from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        newnums = Counter(nums)
        for i in newnums.keys():
            if newnums[i] == 1:
                return i
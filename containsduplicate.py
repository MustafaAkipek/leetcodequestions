from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newnums = Counter(nums)
        for i in newnums.values():
            if i > 1:
                return True
        
        return False
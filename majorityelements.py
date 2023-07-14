from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxrepeat = 0
        maxrepeatnumber = 0
        newnums = Counter(nums)
        for i in newnums.keys():
            if newnums[i] > maxrepeat:
                maxrepeat = newnums[i]
                maxrepeatnumber = i
        
        return maxrepeatnumber
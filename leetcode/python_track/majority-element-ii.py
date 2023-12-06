class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter 
        counter = Counter(nums)
        res = []
        for i in counter.keys():
            if counter[i] > (len(nums) / 3):
                res.append(i)
        return res
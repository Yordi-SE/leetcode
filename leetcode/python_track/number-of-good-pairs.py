class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        count = 0
        for i in counter.keys():
            count += ((counter[i] * (counter[i] - 1)) // 2)
        return count
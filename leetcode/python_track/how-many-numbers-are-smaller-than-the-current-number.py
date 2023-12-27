class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ls = [0] * len(nums)
        for u,i in enumerate(nums):
            for j in nums:
                if j < i:
                    ls[u] += 1
        return ls
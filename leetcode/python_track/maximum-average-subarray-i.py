class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        x = 0
        y = k
        prefix = 0
        avg = float("-inf")
        for i in range(k):
            prefix += nums[i]
        while y <len(nums):
            avg = max(avg, prefix/k)
            prefix += nums[y]
            prefix -= nums[x]
            x += 1
            y += 1
        avg = max(avg, prefix / k)
        return avg
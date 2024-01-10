class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,sums, minlen = 0,0, float('inf')
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= target:
                minlen = min(minlen, i - l + 1)
                sums -= nums[l]
                l += 1
        if minlen == float('inf'):
            return 0
        return minlen
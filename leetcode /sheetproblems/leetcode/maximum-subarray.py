class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = []
        i = 0
        curr_sum = 0
        while i < len(nums):
            if curr_sum < 0:
                curr_sum = max(curr_sum,nums[i])
            else:
                curr_sum += nums[i]
            res.append(curr_sum)
            i += 1
        if len(res) == 0:
            return 0
        return max(res)
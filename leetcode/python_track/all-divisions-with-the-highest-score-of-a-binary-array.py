class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        # print(prefix)
        maxs = float('-inf')
        res = {}
        for i in range(len(prefix) + 1):
            if i == 0:
                left = 0
                right = prefix[len(nums) -1]
            elif i ==len(nums):
                right = 0
                left = (i - 1 + 1) - prefix[i - 1]
            else:
                left = (i - 1 + 1) - prefix[i - 1]
                right = prefix[len(nums) -1] - prefix[i - 1]
            total = left + right
            res[i] = total
            maxs = max(total, maxs)
        # print(res)
        res2 = []
        for i in res:
            if res[i] == maxs:
                res2.append(i)
        return res2
        # return counter
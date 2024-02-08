class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1] + nums[i])
        res = []
        for i in range(len(prefix)):
            if i == 0:
                res.append((nums[i] * i) - (nums[i] * (len(nums) -i - 1)) + ((prefix[len(nums) - 1] - prefix[i])))
            else:
                res.append((nums[i] * i) - (nums[i] * (len(nums) -i - 1)) + ((prefix[len(nums) - 1] - prefix[i]) - (prefix[i-1])))

        return res
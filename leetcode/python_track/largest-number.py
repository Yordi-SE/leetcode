class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums.count(0) == len(nums):
            return "0"
        for i in nums:
            for u in range(len(nums)):
                try:
                    if int(str(nums[u]) + str(nums[u + 1])) < int(str(nums[u + 1]) + str(nums[u])):
                        nums[u], nums[u + 1] = str(nums[u + 1]), str(nums[u])
                    else:
                        nums[u] = str(nums[u])
                except:
                    nums[u] = str(nums[u])
        r = "YORDANOS"
        print(str(r))
        return "".join(nums)
        
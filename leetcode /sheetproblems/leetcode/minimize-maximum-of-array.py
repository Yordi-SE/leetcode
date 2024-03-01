class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        nums2 = sorted(nums)
        res = []
        maxs = nums[0]
        prefix = list(accumulate(nums))
        print(prefix)
        for i in range(1,len(nums)):
            # if nums[i] > nums[i - 1] and nums[i] > 0:
            avg = math.ceil(prefix[i] / (i + 1))
            maxs = max(maxs, avg)
                # print(sums,(sums // (i + 1))+ (sums % (i + 1)),nums[i],i+1)
        # if maxs == float('-inf'):
        #     return max(nums)
        return maxs
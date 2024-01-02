class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        holder = 0
        seeker = 0
        while seeker < len(nums) and holder < len(nums):
            if nums[holder] == 0 and nums[seeker] != 0 and holder < seeker:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
            # print(nums[holder], nums[seeker])
            if nums[holder] != 0:
                holder += 1
            seeker += 1


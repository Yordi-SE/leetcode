class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swaped = False
        for i in nums:
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j],nums[j + 1] = nums[j + 1], nums[j]
                    swaped = True
            if swaped == False:
                break
            swaped = False

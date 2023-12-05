class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        for i in range(1, len(nums)):
            if modified == False and nums[i] < nums[i - 1]:
                if i + 1 < len(nums) and nums[i- 1] < nums[i + 1]:
                    nums[i] = nums[i - 1]
                elif i + 1 < len(nums) and nums[i -1] > nums[i + 1]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                modified = True
            elif modified == True and nums[i] < nums[i - 1]:
                print(nums)
                return False
        print(nums)
        sorted_one = sorted(nums)
        if sorted_one != nums:
            return False
        return True
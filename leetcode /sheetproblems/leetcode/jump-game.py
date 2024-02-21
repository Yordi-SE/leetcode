class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pointer = len(nums) - 1
        i = len(nums) - 1
        while i >= 0:
            for j in range(i-1,-1,-1):
                # print(nums[j],i-j)
                if nums[j] >= i - j:
                    i = j
                    break
            else:
                if i != 0:
                    return False
            if i == 0:
                break
        return True
                
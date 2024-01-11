class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        x = 0
        y = 0
        count = 0
        counter = 0
        while y < len(nums):
            if nums[y] == 0:
                counter += 1
            while counter > k:
                if nums[x] == 0:
                    counter -= 1
                x += 1
            if (y - x + 1) > count:
                count = y - x + 1
            y += 1
        return count
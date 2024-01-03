class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        y = x + 1
        res = [nums[x]]
        while y < len(nums):
            if nums[x] == nums[y]:
                y += 1
            elif nums[x] != nums[y]:
                res.append(nums[y])
                x = y
                y += 1
        for i in range(len(res)):
            nums[i] = res[i]
        return len(res)
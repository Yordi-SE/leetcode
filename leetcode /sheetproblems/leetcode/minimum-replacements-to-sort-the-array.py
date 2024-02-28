class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = []
        curr = nums[-1]
        tl = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i] <= curr:
                curr = nums[i]
            elif nums[i] > curr:
                elem = (nums[i] // curr)
                if (nums[i] % curr):
                    elem +=1
                # print((nums[i] // curr),nums[i] % curr,curr,nums[i],elem)
                tl += (elem - 1)
                curr = (nums[i] // elem)
        return tl

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono_stack = []
        res = [-1] * len(nums)
        for i in range(2 * len(nums)):
            i = i % (len(nums))
            while mono_stack and mono_stack[-1][1] < nums[i]:
                ans = mono_stack.pop()
                res[ans[0]] = nums[i]
            mono_stack.append((i,nums[i]))
        return res
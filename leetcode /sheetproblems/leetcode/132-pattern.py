class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mins = float('inf')
        hashmap = {}
        poped_min = float('inf')
        for i in range(len(nums)):
            while stack and stack[-1] < nums[i]:
                # print(stack)
                poped_min = min(stack.pop(),poped_min)
                # print(mins)
                # print(stack)
            # print(mins,nums[i],stack[-1])
            hashmap[nums[i]] = poped_min
            if stack and hashmap[stack[-1]] < nums[i] < stack[-1]:
                # print(mins,stack[-1],nums[i])
                return True
            stack.append(nums[i])
            mins = min(poped_min,mins)
        return False
                
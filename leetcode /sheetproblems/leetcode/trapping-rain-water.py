class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        maxs = float('-inf')
        trapped = 0
        for i in range(len(height)):
            while stack and maxs < height[i]:
                popped = stack.pop()
                trapped += (maxs - popped)
            maxs = max(maxs,height[i])
            stack.append(height[i]) 
        # print(stack)
        # if stack:
        maxs = float('-inf')
        while stack:
            maxs = max(maxs,stack.pop())
            if stack and stack[-1] <maxs:
                trapped += (maxs - stack[-1])
        return trapped
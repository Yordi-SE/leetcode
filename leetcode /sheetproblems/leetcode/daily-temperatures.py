class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = []
        res = [0] * len(temperatures)
        for i, a in enumerate(temperatures):
            while mono_stack and temperatures[mono_stack[-1]] < temperatures[i]:
                index = mono_stack.pop()
                res[index] = i - index
            mono_stack.append(i)
        return res
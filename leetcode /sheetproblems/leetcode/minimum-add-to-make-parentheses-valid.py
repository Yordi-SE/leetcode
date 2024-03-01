class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            elif stack:
                stack.pop()
            else:
                count += 1
        return len(stack) + count
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        i = 0
        score = {}
        while i < len(s):
            if s[i] == "(":
                stack.append([i,s[i]])
            elif stack:
                poped = stack.pop()
                if i > poped[0] + 1:
                    sums = 0
                    ls = list(score.keys())
                    for j in ls:
                        if poped[0] <= j <= i:
                            sums += score[j]
                            del score[j]
                    score[i] = (2 * sums)
                elif i == poped[0] + 1:
                    score[i] = (1)
            i += 1

        return sum(score.values())
            
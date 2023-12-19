class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) <= k:
            return "".join(list(reversed(list(s))))
        res = [0] * len(s)
        for i in range(0, len(s), 2 * k):
            if i + k - 1 >= len(s):
                ranges = len(s) - 1
            else:
                ranges = i + k - 1
            for j in range(ranges,i - 1, -1):
                if j >= len(s):
                    break
                res[ranges -j + i] = s[j]
        for i in range(len(s)):
            if res[i] == 0:
                res[i] = s[i]
        return "".join(res)
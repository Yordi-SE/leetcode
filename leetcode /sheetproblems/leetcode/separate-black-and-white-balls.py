class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(map(int, list(s)))
        s1 = deepcopy(s)
        r = len(s) - 1
        l = 0
        count = 0
        while l < r:
            while l < r and s[r] != 0:
                r -= 1
            while l < r and s[l] != 1:
                l += 1
            if s[r] == 0 and s[l] == 1:
                count += (r - l)
                r -= 1
                l += 1
        return count
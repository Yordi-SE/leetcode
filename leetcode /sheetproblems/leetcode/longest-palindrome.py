class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        odd = 0
        res = 0
        res2 = 0
        for i in counter:
            if counter[i] % 2 == 0:
                res += counter[i]
            else:
                odd = max(odd, counter[i]) 
                res2 += (counter[i] - 1)
        if odd == 0 and res2 == 0:
            return res
        return max(odd, res2 + 1) + res
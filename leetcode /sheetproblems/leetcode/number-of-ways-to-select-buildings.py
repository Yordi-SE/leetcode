class Solution:
    def numberOfWays(self, s: str) -> int:
        count1,count0= 0,0
        s = list(map(int,s))
        res = 0
        prefix = list(accumulate(s))
        for i in range(len(s)):
            if s[i] == 0:
                count0 += 1
            elif s[i] == 1:
                res += ((((len(s)) - (i + 1)) - (prefix[len(s) - 1] - prefix[i])) * count0)

        for i in range(len(s)):
            if s[i] == 1:
                count1 += 1
            elif s[i] == 0:
                res += ((prefix[len(s) - 1] - prefix[i]) * count1)
                # print(i,)

        return res
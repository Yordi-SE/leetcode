class Solution:
    def balancedString(self, s: str) -> int:
        l = 0
        counter = Counter(s)
        letters = ["W", "Q", "R", "E"]
        seta = []
        n = len(s) // 4
        for i in letters:
            if counter[i] > n:
                seta.append(i)
        res = {}
        res1 = {}
        for i in seta:
            res[i] = (counter[i] - n)
            res1[i] = 0
        minlen = float('inf')
        for r in range(len(s)):
            if len(seta) == 0:
                return 0
            if s[r] in seta:
                res1[s[r]] += 1
            for i in seta:
                if res1[i] < res[i]:
                    break
            else:
                for i in seta:
                    while res1[i] > res[i]:
                        for v in seta:
                            if res1[v] < res[v]:
                                break
                        else:
                            minlen = min(minlen, r - l + 1)
                        if s[l] in seta:
                            res1[s[l]] -= 1
                            if res1[s[l]] <= res[s[l]]:
                                l += 1
                                break
                        l += 1
            if res1 == res:
                while s[l] not in seta:
                    l += 1
                minlen = min(minlen, r - l + 1)
        return minlen
            


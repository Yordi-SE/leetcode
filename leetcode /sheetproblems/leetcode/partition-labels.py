class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter = Counter(s)
        seta = set()
        l = 0
        res = []
        for i in range(len(s)):
            counter[s[i]] -= 1
            seta.add(s[i])
            for j in seta:
                if counter[j] != 0:
                    break
            else:
                res.append(i - l + 1)
                l = i + 1
                seta = set()
                
        return res
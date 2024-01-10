class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap1 = Counter(s1)
        hashmap2 = {}
        if len(s2) < len(s1):
            return False
        for i in range(len(s1)):
            if s2[i] in hashmap1:
                if s2[i] in hashmap2:
                    hashmap2[s2[i]] += 1
                else:
                    hashmap2[s2[i]] = 1
        if hashmap2 == hashmap1:
            return True
        l = 0
        r = len(s1)
        while r < len(s2):
            if s2[r] in hashmap1:
                if s2[r] in hashmap2:
                    hashmap2[s2[r]] += 1
                else:
                    hashmap2[s2[r]] = 1
            if s2[l] in hashmap1:
                if s2[l] in hashmap2 and hashmap2[s2[l]] <= 1:
                    del hashmap2[s2[l]]
                else:
                    hashmap2[s2[l]] -= 1
            if hashmap2 == hashmap1:
                return True
            l += 1
            r += 1
        return False
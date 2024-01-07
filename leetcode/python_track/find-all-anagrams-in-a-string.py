class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        x = 0
        y = x + len(p)
        res = []
        hashmap = {}
        hashmap_2 = {}
        check = False
        if len(p) > len(s):
            return []
        for i in p:
            if i in hashmap.keys():
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in range(x,y):
            if s[i] in hashmap_2.keys():
                hashmap_2[s[i]] += 1
            else:
                hashmap_2[s[i]] = 1
        
        while y < len(s) + 1:
            if hashmap == hashmap_2:
                res.append(x)
            if s[x] in hashmap_2.keys():
                if hashmap_2[s[x]] <= 1:
                    del hashmap_2[s[x]]
                else:
                    hashmap_2[s[x]] -= 1
            if y < len(s) and s[y] in hashmap_2.keys():
                hashmap_2[s[y]] += 1
            elif y < len(s):
                hashmap_2[s[y]] = 1
            x += 1
            y += 1
        return res
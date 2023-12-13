class Solution:
    def minimizedStringLength(self, s: str) -> int:
        hashmap = {}
        for i, u in enumerate(s):
            if u in hashmap.keys():
                hashmap[u].append(i)
            else:
                hashmap[u] = [i]
        lens = len(s)
        for i in hashmap.keys():
            n = len(hashmap[i])
            while n >= 2:
                if n == 2:
                    n -= 1
                    lens = lens - 1
                else:
                    n -= 2
                    lens = lens - 2
        return lens
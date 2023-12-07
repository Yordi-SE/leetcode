class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        hashmap = {}
        res = ""
        for i in spaces:
            hashmap[i] = 0
        for i in range(len(s)):
            if i in hashmap.keys():
                res += " "
            res += s[i]
        return res
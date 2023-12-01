class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        if len(word1) <= len(word2):
            lens = len(word1)
            longer = word2
        else:
            lens= len(word2)
            longer = word1
        for i in range(lens):
            res += (word1[i] + word2[i])
        if lens < len(longer):
            res += longer[lens:]
        return res
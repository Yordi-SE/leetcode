class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter = 0
        res = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                res += strs[j][i]
            if res != "".join(list(sorted(res))):
                counter += 1
            res  = ""
        return counter
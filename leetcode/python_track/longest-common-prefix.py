class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = ""
        lens = float('inf')
        for j in strs:
            if len(j) < lens:
                lens = len(j)
        for i in range(lens):
            index = False
            for j in (range(1, len(strs))):
                print(strs[j][i:])
                if strs[0][i] != strs[j][i]:
                    index = True
                    break
            if index == False:
                temp += strs[0][i]
            elif index == True:
                break
        return temp
                
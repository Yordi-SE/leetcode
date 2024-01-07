class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x = 0
        y = x + 1
        if len(s) == 0:
            return 0
        subarray = [s[x]]
        temp = 1
        while y < len(s):
            if s[y] not in subarray:
                subarray.append(s[y])
                y += 1
            elif s[y] in subarray:
                subarray.remove(s[x])
                x += 1
            if len(subarray) > temp:
                temp = len(subarray)
        if len(subarray) > temp:
            temp = len(subarray)
        return temp
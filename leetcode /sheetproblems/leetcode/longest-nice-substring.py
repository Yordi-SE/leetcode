class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def helper(s2):
            seta = set(s2)
            if len(s2) <2:
                return ""
            for i in range(len(s2)):
                if not (s2[i].lower()  in seta and s2[i].upper() in seta):
                    val = helper(s2[:i])
                    val1 = helper(s2[i+1:])
                    if len(val1) > len(val):
                        return val1
                    else:
                        return val
            return s2
        return helper(s)

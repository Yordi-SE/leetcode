class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        romans = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        while i < len(s):
            if (i + 1) < len(s):
                if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
                    res += (romans[s[i + 1]] - romans[s[i]])
                    i += 1
                elif s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
                    res += (romans[s[i + 1]] - romans[s[i]])
                    i += 1
                elif s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
                    res += (romans[s[i + 1]] - romans[s[i]])
                    i += 1
                else:
                    res += romans[s[i]]
            else:
                res += romans[s[i]]
            i += 1
        return res
            
                
        
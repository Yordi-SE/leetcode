class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l , r = 0, 0
        count = {s[0] : 1}
        while r < len(s):
            check = len(s[l:r + 1]) - max(count.values())
            if check <= k:
                r += 1
                if r < len(s):
                    if s[r] in count.keys():
                        count[s[r]] += 1
                    else:
                        count[s[r]] = 1
                    if len(s[l: r + 1]) - max(count.values()) <= k:
                        if res < len(s[l: r + 1]):
                            res = len(s[l:r + 1])
            elif check > k:
                count[s[l]] -= 1
                l += 1
        return  res 
            

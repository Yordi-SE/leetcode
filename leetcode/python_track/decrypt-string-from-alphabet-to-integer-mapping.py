class Solution:
    def freqAlphabets(self, s: str) -> str:
        maps = {}
        res = ""
        for i in range(97, 123):
            maps[str(26 - (122 - i))] = chr(i)
        print(maps)
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                if i - 1 >= 0 and i - 2 >= 0:
                    if s[i -1] != "#" and s[i - 2] != "#":
                        res += maps[s[i - 2:i]]
                        i -= 2
            else:
                res += maps[s[i]]
            i -= 1
        return "".join(list(reversed(res)))

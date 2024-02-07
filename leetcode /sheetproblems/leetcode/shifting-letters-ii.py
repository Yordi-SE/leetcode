class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        hashmap = defaultdict(int)
        hashmap2 = defaultdict(int)
        for i in range(26):
            hashmap[chr(97 + i)] = i
        s = list(s)
        for i in range(len(s)):
            s[i] = hashmap[s[i]]
        s2 = [0] * len(s)
        for i in range(26):
            hashmap2[i] =  chr(97 + i)
        for i in shifts:
            if i[2] == 1:
                s2[i[0]] += 1
                if i[1] + 1 < len(s2):
                    s2[i[1] + 1] -= 1
            if i[2] == 0:
                s2[i[0]] -= 1
                if i[1] + 1 < len(s2):
                    s2[i[1] + 1] += 1
        res = [s2[0]]
        for i in range(1,len(s2)):
            res.append(res[-1] + s2[i])
        # print(res)
        # print(s)
        for i in range(len(s)):
            if s[i] + res[i] > 25:
                # print(s[i] + res[i] - 26,(s[i],res[i]))
                s[i] = hashmap2[(s[i]+res[i])%26]
            elif s[i] + res[i] < 0:
                # print(26 - (s[i]+res[i]),(s[i],res[i]))
                s[i] = hashmap2[(s[i]+res[i])%26]
            else:
                # print(s[i]+res[i],(s[i],res[i]))
                s[i] = hashmap2[s[i]+res[i]]
        # print(hashmap2)
        return "".join(s)
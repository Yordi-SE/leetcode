class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = defaultdict(int)
        t_hash = defaultdict(int)

        for i in t:
            t_hash[i] += 1
            check[i] = 0
        res = []
        l = 0
        for r in range(len(s)):
            if s[r] in t_hash:
                check[s[r]] += 1
            for i in t_hash:
                if check[i] < t_hash[i]:
                    break
            else:
                for i in t_hash:
                    while check[i] > t_hash[i]:
                        for v in t_hash:
                            if check[v] < t_hash[v]:
                                break
                        else:
                            
                            if len(res) != 0 and  r - l + 1 <= res[1] - res[0] + 1:
                                res = [l,r]
                            elif  len(res) == 0:
                                res = [l, r]
                        if s[l] in t_hash:
                            if check[s[l]] > t_hash[s[l]]:
                                check[s[l]] -= 1
                            else:
                                break
                        l += 1

            if check == t_hash:
                while s[l] not in t_hash:
                    l += 1
                if len(res) != 0 and  r - l + 1 <= res[1] - res[0] + 1:
                    res = [l,r]
                elif  len(res) == 0:
                    res = [l, r]
        if len(res) == 0:
            return ""
        return s[res[0]:res[1]+1]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        s = ""
        for i in range(26):
            s += chr(123-(26-i))
        hashmap = {}
        l = 2
        for i in range(0,26,3):
            hashmap[l] = s[i:i+3]
            l += 1
        hashmap[7] += hashmap[8][0]
        hashmap[8] = "tuv"
        hashmap[9] = "wxyz"
        # print(hashmap)
        ans = []
        def backtrack(num,comp,j):
            # print(num)
            if len(num) == len(digits) and len(num) > 0:
                ans.append("".join(comp[:]))
                return
            if j >= len(digits):
                # ans.append(comp)
                return

            k = int(digits[j])
            for i in range(len(hashmap[k])):
                comp.append(hashmap[k][i])
                num.append(k)

                backtrack(num,comp,j + 1)
                comp.pop()
                num.pop()
        backtrack([],[],0)
        return ans
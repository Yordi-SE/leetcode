class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        res = []
        for i, u in enumerate(words):
            found = False
            u = u.lower()
            if u[0] in first_row:
                must_be = 1
            if u[0] in second_row:
                must_be = 2
            if u[0] in third_row:
                must_be = 3
            for j in u:
                if j in first_row and must_be != 1:
                    found = True
                elif j in third_row and must_be != 3:
                    found = True
                elif j in second_row and must_be != 2:
                    found = True
            if found == False:
                res.append(words[i])
        return res                

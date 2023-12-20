class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res, res2, res3 = [], [], []
        for i in range(len(mat[0]) + len(mat) - 1):
            if i >= len(mat[0]):
                index = len(mat) - ((len(mat[0]) + len(mat) - 1) - i)
                i = len(mat[0]) - 1
                for j in range(index, len(mat)):
                    res.append(mat[j][i])
                    i -= 1
                    if i <0:
                        break
                res2.append(res)
                res = []   
            else:             
                for j in range(len(mat)):
                    res.append(mat[j][i])
                    i -= 1
                    if i <0:
                        break
                res2.append(res)
                res = []
        for i in range(0,len(res2), 2):
            res2[i] = res2[i][::-1]
        for i in range(len(res2)):
            res3 += res2[i]
        return res3
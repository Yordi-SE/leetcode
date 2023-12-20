class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res, res2 = [], []
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                res.append(matrix[j][i])
            res2.append(res)
            res = []
        return res2
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sums = 0
        for i in range(len(mat)):
            sums += mat[i][i]
            print(mat[i][i])
        for i in range(len(mat) - 1, -1, -1):
            sums += mat[len(mat) - i - 1][i]
        if len(mat) % 2:
            sums -= mat[len(mat)//2][len(mat)//2]
        return sums
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[matrix[0][0]]]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if j == 0 and i != 0:
                    self.prefix.append([self.prefix[-1][j] + matrix[i][j]])
                if i == 0 and j != 0:
                    self.prefix[i].append(self.prefix[0][-1] + matrix[0][j])
                if i != 0 and j != 0:

                    self.prefix[i].append(self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1] + matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col1 != 0 and row1!= 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1] - self.prefix[row1-1][col2] + self.prefix[row1-1][col1-1]
        elif col1 == 0 and row1 != 0:
            return self.prefix[row2][col2]  - self.prefix[row1-1][col2]
        elif col1!= 0 and row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1]
        return self.prefix[row2][col2]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_maxs = []
        col_maxs = []
        for i in range(len(grid)):
                row_maxs.append(max(grid[i]))
        for i in range(len(grid)):
            cols = []
            for j in range(len(grid)):
                cols.append(grid[j][i])
            col_maxs.append(max(cols))
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                count += (min(row_maxs[i],col_maxs[j]) - grid[i][j])
        # print(row_maxs)
        # print(col_maxs)
        return count
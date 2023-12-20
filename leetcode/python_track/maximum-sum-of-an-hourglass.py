class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                try:
                    if len(grid[i][j:j + 3]) == 3:
                        sums = sum(grid[i][j:j + 3]) + sum(grid[i + 2][j:j+3]) + grid[i + 1][j + 1]
                        res.append(sums)
                except IndexError:
                    continue
        return max(res)
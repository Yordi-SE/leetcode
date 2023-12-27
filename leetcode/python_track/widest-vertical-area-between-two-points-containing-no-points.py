class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])
        width = float('-inf')
        for i in range(1,len(points)):
            width = max(width, points[i][0] - points[i - 1][0])
        return width
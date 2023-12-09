class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        counter = 0
        for i in range(1,len(points)):
            distance = max(abs(points[i - 1][0] - points[i][0]), abs(points[i - 1][1] - points[i][1]))
            counter += distance


        return counter
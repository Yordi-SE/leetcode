class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[1],x[0]))
        # print(points)
        arrows = 0
        i = 0
        while i < len(points):
            j = i + 1
            while j < len(points):
                if points[j][0] > points[i][1]:
                    break
                j += 1
            i = j
            
            arrows += 1
        return arrows
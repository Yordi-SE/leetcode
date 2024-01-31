class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        second = 0
        res = []
        if len(secondList) == 0 or len(firstList) == 0:
            return res
        for first in range(len(firstList)):
            # while 0< second < len(secondList) and firstList[first][1] >= secondList[second][0] and firstList[first][0] <= secondList[second][1]:
            #     second -= 1
            while second < len(secondList):
                if second < len(secondList) and firstList[first][1] >= secondList[second][0] and firstList[first][0] <= secondList[second][1]:
                    res.append([max(firstList[first][0],secondList[second][0]),min(firstList[first][1],secondList[second][1])])
                elif second < len(secondList) and  firstList[first][1] < secondList[second][0]:
                    break
                second += 1
            second = 0
        return res
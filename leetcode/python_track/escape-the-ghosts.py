class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        distance = lambda x1, x2, y1, y2: (((x1 - x2) ** 2) + ((y1 - y2) ** 2))**0.5
        res = []
        for i in ghosts:
            res.append(round(distance(i[0], target[0], target[1], target[1]), 5)+ round(distance(target[0], target[0], i[1], target[1]), 5))
        print(res)
        maxs = min(res)
        print(maxs)
        
        if round(distance(target[0], target[0], 0, target[1]), 5) + round(distance(0, target[0], target[1], target[1]), 5) < maxs:
            return True
        return False
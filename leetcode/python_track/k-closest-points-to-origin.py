class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        list1 = []
        list2 = []
        for i in points:
            m = round((i[0]**2 + i[1]**2)**0.5, 3)
            list1.append(m)
        list3 = list1.copy()
        list1.sort()
        for i in list1[:k]:
            for u, j in enumerate(list3):
                if j == i:
                    list2.append(points[u])
                    del points[u]
                    del list3[u]
                    break
        return list2
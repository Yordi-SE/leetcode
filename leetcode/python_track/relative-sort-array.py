class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        maxi = max(arr1)
        res = []
        counter = [0] * (maxi + 1)
        for i in arr1:
            counter[i] += 1
        for j in arr2:
            for i, a in enumerate(counter):
                if i == j:
                    while a > 0:
                        res.append(i)
                        a -= 1
        for i, a in enumerate(counter):
            if i not in arr2:
                while a > 0:
                    res.append(i)
                    a -= 1
        return res
        


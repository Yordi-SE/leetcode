class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maximum = max(heights)
        counter = [0] * (maximum + 1)
        names2 = [0] * len(names)
        res = [0] * len(heights)
        for i in heights:
            counter[i] += 1
        x = len(heights) - 1
        for i, a in enumerate(counter):
            while a > 0:
                res[x] = i
                x -= 1
                a -= 1
        for i, a in enumerate(res):
            index = heights.index(a)
            names2[i] = names[index]

        return names2

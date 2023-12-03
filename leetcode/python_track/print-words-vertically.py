class Solution:
    def printVertically(self, s: str) -> List[str]:
        list1 = s.split()
        lens = len(list1[0])
        longer = list1[0]
        index = 0
        for i, u in enumerate(list1):
            if len(u) > lens:
                lens = len(u)
                longer = u
                index = i
        res = ""
        ress = []
        print(list1)
        for i in range(lens):
            for j in range(len(list1)):
                if i < len(list1[j]):
                    res += list1[j][i]
                    ind = j
                else:
                    res += " "
            ress.append(res[:ind + 1])
            res = ""
        return ress
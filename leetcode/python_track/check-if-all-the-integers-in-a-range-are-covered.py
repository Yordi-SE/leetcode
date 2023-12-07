class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        counter = 0
        list1 = list(range(left, right+ 1))

        for i in list1:
            for j in ranges:
                if j[0] <= i <= j[1]:
                    counter +=1
                    break
        return len(list1) == counter

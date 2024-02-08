class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxk = float('-inf')
        for i in range(len(trips)):
            maxk = max(maxk,trips[i][2])
        prefix = [0] * (maxk + 1)
        n = len(prefix)
        for i in trips:
            prefix[i[1]] += i[0]
            if i[2]  < n:
                prefix[i[2]] -= i[0]
        prefix2 = [prefix[0]]
        for i in range(1,len(prefix)):
            prefix2.append(prefix2[-1] + prefix[i])
        for i in range(len(prefix)):
            if prefix2[i] > capacity:
                return False
        return True
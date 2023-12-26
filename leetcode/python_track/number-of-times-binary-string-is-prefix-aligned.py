class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        counter = 0
        maxs = float('-inf')
        for i in range(1,len(flips) + 1):
            count += 1
            maxs = max(flips[i - 1], maxs)
            if count == i and i == maxs:
                counter += 1
        return counter

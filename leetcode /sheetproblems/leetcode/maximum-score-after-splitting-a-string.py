class Solution:
    def maxScore(self, s: str) -> int:
        list1 = list(map(int,list(s)))
        prefix = [list1[0]]
        for i in range(1,len(list1)):
            prefix.append(prefix[-1] + list1[i])
        maxs = float('-inf')
        for i in range(1,len(list1)):
            maxs = max(maxs,i - prefix[i - 1] + (prefix[len(list1) - 1] - prefix[i-1]))
        if maxs == float('-inf'):
            return 0
        return maxs
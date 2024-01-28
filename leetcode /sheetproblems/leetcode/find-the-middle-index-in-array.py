class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = []
        for i in nums:
            if len(prefix) != 0:
                prefix.append(i + prefix[-1])
            else:
                prefix.append(i)
        for i in range(len(prefix)):
            if i == 0:
                if prefix[-1] - prefix[i] == 0:
                    return i
            elif i == (len(nums)) -1:
                if prefix[i - 1] == 0:
                    return i
            elif prefix[i - 1] == prefix[-1] - prefix[i]:
                return i
        return -1
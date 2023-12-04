class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        counter = 0
        for i in nums:
            if i == 1:
                counter +=1
            elif i == 0:
                counter = 0
            if res < counter:
                res = counter
        return res
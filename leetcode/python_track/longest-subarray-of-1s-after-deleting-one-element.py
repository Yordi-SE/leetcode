class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,r,counter,maxlen = 0,0,0,float('-inf')
        while r < len(nums):
            if nums[r] == 0:
                counter += 1
            while counter >1:
                if nums[l] == 0:
                    counter -= 1
                l += 1
            maxlen = max(maxlen, r - l)
            r += 1
        return maxlen
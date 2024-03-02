class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix = list(accumulate(nums))
        if prefix[-1] % p == 0:
            return 0
        k = prefix[-1] % p
        hashmap = {}
        hashmap[0] = -1
        count = float('inf')
        for i in range(len(prefix)):
            reminder = (prefix[i] % p) - k
            if reminder < 0:
                reminder += p
            if reminder in hashmap:
                count = min(count, (i - (hashmap[reminder])))
            hashmap[prefix[i] % p] = i
        if count >= len(nums):
            return -1
        return count
        # return 1
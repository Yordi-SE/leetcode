class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        r, l,sums,maxsum = 0, 0,0, float('-inf')
        hashmap = {}
        while r < len(nums):
            if nums[r] in hashmap:
                hashmap[nums[r]] += 1
                while hashmap[nums[r]] > 1:
                    if hashmap[nums[l]] <= 1:
                        del hashmap[nums[l]] 
                    else:
                        hashmap[nums[l]] -= 1
                    sums -= nums[l]
                    l += 1
            elif nums[r] not in hashmap:
                hashmap[nums[r]] = 1
            sums += nums[r]
            # print(hashmap)

            r += 1
            maxsum = max(maxsum, sums)
        return maxsum
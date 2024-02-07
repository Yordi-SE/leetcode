class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix, counter = 0, 0
        hashmap = {0: 1}
        for i in range(len(nums)):
            prefix += nums[i]
            difference = prefix - k
            if difference in hashmap.keys():
                counter += hashmap[difference]
            if prefix in hashmap.keys():
                hashmap[prefix] += 1
            if prefix not in hashmap.keys():
                hashmap[prefix] = 1
        return counter
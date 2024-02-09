class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        from itertools import accumulate
        prefix = list(accumulate(nums))
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0
        for i in range(len(prefix)):
            diff = prefix[i] - goal
            if diff in hashmap:
                count += hashmap[diff]
                # print(count)
            hashmap[prefix[i]] += 1
            # print(hashmap)
            # print("======================================")
        return count
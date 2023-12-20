class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        hashmap = {}
        counter = 0
        for i in range(len(nums)):
            if nums[i] in hashmap:
                for j in hashmap[nums[i]]:
                    if (j * i) % k == 0:
                        counter += 1
                hashmap[nums[i]].append(i)
            else:
                hashmap[nums[i]] = [i]
        return counter
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(list)
        res = [0] * len(nums)
        for i in range(len(nums)):
            hashmap[nums[i]].append(i)
        for i in hashmap:
            if len(hashmap[i])> 1:
                prefix = [hashmap[i][0]]
                for j in range(1,len(hashmap[i])):
                    prefix.append(prefix[-1] + hashmap[i][j])
                for j in range(len(prefix)):
                    if j == 0:
                        res[hashmap[i][j]] = ((hashmap[i][j] * j) - (hashmap[i][j] * (len(hashmap[i]) -j - 1)) + ((prefix[len(hashmap[i]) - 1] - prefix[j])))
                    else:
                        res[hashmap[i][j]] = ((hashmap[i][j] * j) - (hashmap[i][j] * (len(hashmap[i]) -j - 1)) + ((prefix[len(hashmap[i]) - 1] - prefix[j]) - (prefix[j-1])))
        return res
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix2 = [0] * len(nums)
        nums.sort(reverse=True)
        for i in requests:
            prefix2[i[0]] += 1
            if i[1] + 1 < len(nums):
                prefix2[i[1] + 1] -= 1
        prefix = [prefix2[0]]
        for i in range(1,len(prefix2)):
            prefix.append(prefix[-1]+prefix2[i])
        hashmap = defaultdict(int)
        for i,u in enumerate(prefix):
            hashmap[i] = u
        hashmap = sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        res = [0] * len(nums)
        for i in range(len(hashmap)):
            res[hashmap[i][0]] = nums[i]
        prefix = [res[0]]
        for i in range(1,len(res)):
            prefix.append(prefix[-1]+res[i])
        res2 = []
        for i in requests:
            if i[0] == 0:
                res2.append(prefix[i[1]])
            else:
                res2.append(prefix[i[1]] - prefix[i[0] - 1])
        return sum(res2)%(10**9 + 7)
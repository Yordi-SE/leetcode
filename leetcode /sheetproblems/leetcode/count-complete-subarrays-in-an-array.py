class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        distinct = len(set(nums))
        count,count2 = 0,0
        l = 0
        for r in range(len(nums)):
            hashmap[nums[r]] += 1
            # while l <=r and len(hashmap) > distinct:
            #     print(hashmap)
            #     hashmap[nums[l]] -= 1
            #     if hashmap[nums[l]] <= 0:
            #         del hashmap[nums[l]]
            #     print(len(hashmap))
            #     l += 1
           
            if len(hashmap) == distinct:
                hashmap2 = deepcopy(hashmap)
                l = 0
                while l <=r and  len(hashmap2) == distinct:
                    # print(nums[l:r+1],l,r)
                    # print(hashmap2)
                    
                    count2 += 1
                    hashmap2[nums[l]] -= 1
                    if hashmap2[nums[l]] <= 0:
                        del hashmap2[nums[l]]
                    l += 1
                # l -= 1
                # hashmap[nums[l]] += 1
                # print("============================")
                count = count2
        return count
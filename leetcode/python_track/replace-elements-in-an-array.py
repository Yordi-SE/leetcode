class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashmap = {}
        for i, u in enumerate(nums):
            hashmap[u] = i
        for i in operations:
            print(i[0])
            index = hashmap[i[0]]
            nums[index] = i[1]
            hashmap[i[1]] = index
            del hashmap[i[0]]
        return nums
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        temp = []
        for i in range(len(nums)):
            if (2 * i) + 1 < len(nums):
                list1 = [nums[(2 * i) + 1]] * nums[(2 * i)]
                print(list1)
                temp += list1
        return temp
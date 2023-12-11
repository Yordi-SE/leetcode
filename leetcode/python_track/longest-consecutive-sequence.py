class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        counter = 0
        temp = 0
        set1 = set(nums)
        list1 = sorted(list(set1))
        if len(list1) < 2:
            return len(list1)
        for i in range(1,len(list1)):
            if list1[i] - list1[i - 1] == 1:
                counter += 1
            else:
                counter = 0
            temp = max(counter + 1, temp)

        return temp
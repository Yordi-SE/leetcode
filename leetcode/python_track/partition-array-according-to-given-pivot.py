class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1 = []
        list2 = []
        list3 = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                list1.append(nums[i])
            elif nums[i] > pivot:
                list2.append(nums[i])
            else:
                list3.append(nums[i])
        res = list1 + list3 + list2
        for i in range(len(nums)):
            nums[i] = res[i]
        return nums
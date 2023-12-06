class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative_holder = []
        positive_holder = []
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                positive_holder.append(nums[i])
            else:
                negative_holder.append(nums[i])
        for i in range(len(positive_holder)):
            res.append(positive_holder[i])
            res.append(negative_holder[i])
        return res
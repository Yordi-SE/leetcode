class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        k = float('inf')
        for i in nums1:
            ckeck = False
            k = float('inf')
            for j in range(len(nums2)):
                if i == nums2[j]:
                    k = j
                if j > k and nums2[j] > i:
                    res.append(nums2[j])
                    ckeck = True
                    break
            if ckeck == False:
                res.append(-1)
        return res
                

        
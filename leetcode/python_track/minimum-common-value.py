class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first, second = 0, 0
        set1 = set(nums1)
        set2 = set(nums2)
        the_occured = float('inf')
        while first < len(nums1) and second < len(nums2):
            if nums1[first] in set2:
                the_occured = min(the_occured, nums1[first])
            if nums2[second] in set1:
                the_occured = min(the_occured, nums2[second])
            first += 1
            second += 1
        if the_occured == float('inf'):
            return -1
        return the_occured
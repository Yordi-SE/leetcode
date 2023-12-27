class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        res = []
        counter2 = Counter(nums2)
        for i in counter1:
            if i in counter2:
                for j in range(min(counter1[i], counter2[i])):
                    res.append(i)
        return res
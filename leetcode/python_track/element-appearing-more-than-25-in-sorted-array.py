class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        from collections import Counter
        frequency = len(arr) // 4
        counter = Counter(arr)
        for i in counter:
            if counter[i] > frequency:
                return i
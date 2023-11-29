class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1
        while i % n != 0 or i % 2 != 0:
            i += 1
        return i
        
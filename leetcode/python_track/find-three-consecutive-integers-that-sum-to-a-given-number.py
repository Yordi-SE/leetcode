class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        sums = lambda x: (x - 1) + x + (x + 1)
        x = (num // 3)
        if sums(x) == num:
            return [x-1, x, x + 1]
        return []
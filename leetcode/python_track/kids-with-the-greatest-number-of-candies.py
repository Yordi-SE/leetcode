class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxs = max(candies)
        result = []
        for i in candies:
            result.append((i + extraCandies) >= maxs)
        return result
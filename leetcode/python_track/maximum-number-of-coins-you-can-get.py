class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        mine = 0
        p = 1
        for i in range(len(piles) // 3):
            mine += piles[p]
            p += 2
        return mine


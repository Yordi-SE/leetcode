class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, minop,counterW = 0,float('inf'),0
        for i in range(k):
            if blocks[i] == "W":
                counterW += 1
        r = k
        minop = min(minop, counterW)
        while r < len(blocks):
            if blocks[r] == 'W':
                counterW += 1
            if blocks[l] == 'W':
                counterW -= 1
            minop = min(minop, counterW)
            l += 1
            r += 1
        return minop
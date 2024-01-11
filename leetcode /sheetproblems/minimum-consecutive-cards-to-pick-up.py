class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l,minlen= 0, float('inf')
        set1 = set()
        for r in range(len(cards)):
            if cards[r] in set1:
                while cards[l] != cards[r]:
                    set1.discard(cards[l])
                    l += 1

                minlen = min(minlen, r - l + 1)
                l += 1
            else:
                set1.add(cards[r])
        if minlen == float('inf'):
            return -1
        return minlen
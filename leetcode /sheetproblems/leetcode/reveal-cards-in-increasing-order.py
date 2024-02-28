class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = deque()
        res.appendleft(deck[-1])
        for i in range(len(deck)-2,-1,-1):
            poped = res.pop()
            res.appendleft(poped)
            res.appendleft(deck[i])
        return res
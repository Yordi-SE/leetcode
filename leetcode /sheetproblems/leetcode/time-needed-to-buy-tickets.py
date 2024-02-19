class Solution:
    from collections import deque
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        de = deque(tickets)
        count = 0
        while de[k] > 0:
            t = de.popleft()
            if t > 0:
                count += 1
                t -= 1
            de.append(t)
            k -= 1
            k = k % (len(de))
        return count


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints)
        prefix = [cardPoints[0]]
        n = len(cardPoints)

        ans = float('-inf')
        for r in range(1,len(cardPoints)):
            prefix.append(prefix[-1] + cardPoints[r])
        for i in range(len(cardPoints)-(n-k) + 1):
            if i == 0:
                ans = max(ans, total - (prefix[i+  n-k-1]))
            else:
                ans = max(ans, total - (prefix[i + n-k-1] - prefix[i - 1]))
                # print(prefix[i + n-k-1])
                # print(prefix[i - 1])
        return ans
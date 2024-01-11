class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        countF, countT,l,maxlen = 0,0,0,float('-inf')
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                countT += 1
            else:
                countF += 1
            while countF > k and countT > k:
                if answerKey[l] == 'T':
                    countT -= 1
                else:
                    countF -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)
        return maxlen
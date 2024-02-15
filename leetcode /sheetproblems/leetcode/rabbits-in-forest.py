class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        # print(counter)
        for i in counter:
            if i == 0:
                ans += (counter[i])
            elif counter[i] > i + 1:
                ans += ((counter[i] // (i + 1))*(i + 1))
                if counter[i] % (i + 1) > 0:
                    ans += (i + 1)
            else:
                ans += (i + 1)
        return ans
        
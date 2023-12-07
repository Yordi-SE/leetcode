class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        res = 0
        for i in range(weeks):
            for j in range(7):
                res += (i + 1 + j)
            print(res)
        left_days = n%7
        for i in range(left_days):
            res += (weeks + 1 + i)
        return res
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = abs(n)
        if n == 1:
            return x
        elif n == 0:
            return 1
        reminder = n % 2
        if reminder != 0:
            val = x
        else:
            val = 1
        # print(n)
        n = n // 2
        # print(n)
        val2 = self.myPow(x,abs(n))
        res = (val2 * val2 * val)
        return res

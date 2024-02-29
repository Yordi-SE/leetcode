class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # self.countGoodNumbers(n//2)
        if n% 2:
            return ((self.power(n//2,20) * 5) % ((10 ** 9) + 7))
        return ((self.power(n//2,20)) % ((10 ** 9) + 7))
    def power(self,n,x):
        if n == 1:
            return x
        if n == 0:
            return 1
        ans = self.power(n//2,x) 
        if n % 2:
            return (x * ans * ans) % ((10 ** 9) + 7)
        return (ans * ans)% ((10 ** 9) + 7)
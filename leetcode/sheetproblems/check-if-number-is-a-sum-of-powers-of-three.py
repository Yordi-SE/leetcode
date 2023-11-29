class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        temp = n
        while temp > 0:
            if temp % 3 == 2:
                return False
            temp = temp // 3
        return True
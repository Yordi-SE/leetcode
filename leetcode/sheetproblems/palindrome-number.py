class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(str(x))
        y.reverse()
        y = "".join(y)
        if y == str(x):
            return True
        return False
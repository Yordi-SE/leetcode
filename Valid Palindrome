class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        for i in s:
            if not i.isalnum():
                continue
            else:
                ls.append(i.lower())
        if list(reversed(ls)) == ls:
            return True
        return False

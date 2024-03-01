class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) <=1:
            return ""
        s = ""
        palindrome = list(palindrome)
        for i in range(26):
            s += chr(123 -(26 - i))
        hashmap = {}
        for i in range(len(s)):
            hashmap[s[i]] = i
        idx = float('-inf')
        for i in range(len(palindrome)//2):
            if hashmap[palindrome[i]] - 0 > 0:
                palindrome[i] = s[0]
                break
        else:
            palindrome[len(palindrome)-1] = s[hashmap[palindrome[0]] + 1]
        # i = 0
        # while s[i] == palindrome[idx]:
        #     i += 1
        # palindrome[idx] = s[i]
        return "".join(palindrome)
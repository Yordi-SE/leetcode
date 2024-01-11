class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = l + k - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}
        counter1, counter = 0, 0
        for i in range(k):
            if s[i] in vowels:
                counter += 1
        counter1 = counter
        while r < len(s):
            r += 1
            if r < len(s) and s[r] in vowels:
                counter1 += 1
            if s[l] in vowels:
                counter1 -= 1
            counter = max(counter, counter1)
            l += 1
        return counter

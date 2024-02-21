class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.check(0,len(s)-1,s)
    def check(self,pointer1,pointer2,s):
        if pointer1 >= pointer2:
            return
        s[pointer1],s[pointer2] = s[pointer2],s[pointer1]
        self.check(pointer1+1,pointer2-1,s)

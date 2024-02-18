class Solution:
    def isValid(self, s: str) -> bool:
        str1 = '({['
        str2 = ')}]'
        stack = []
        e = 0
        r = 0
        for i in s:
            if i in str1:
                stack.append(i)
                e += 1
            elif i in str2:
                r += 1
                if not stack:
                    return False
                if str2.index(i) != str1.index(stack.pop()):
                    return False
        if r != e:
            return False
        return True
                

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack2 = []
        
        def helper(i):
            if i >= len(s):
                return "".join(stack)
            # s = s.split("]")
            # i =
            # while i < len(s):
            if s[i] != "]" and not s[i].isdigit():
                stack.append(s[i])
                # i += 1
            elif s[i].isdigit():
                s2 = ""
                while s[i].isdigit():
                    s2 += s[i]
                    i += 1
                i -= 1
                stack2.append(s2)
            else:
                s2 = ""
                while stack and stack[-1] != "[":
                    s2 = stack.pop() + s2
                s2 = s2 * int(stack2.pop())
                stack.pop()
                stack.append(s2)
                # i += 1
                
            # s = "".join(s)
            
            return helper(i +1)
        return helper(0)
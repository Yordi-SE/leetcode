class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = '+/*-'
        stack = []
        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                operand1 = (stack.pop())
                operand2 = (stack.pop())
                if i == '/':
                    result = int(eval(operand2 + '/' + operand1))
                else:
                    result = eval(operand2 + i + operand1)
                stack.append(str(result))
        return int(stack[-1])

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        comp = []
        def backtrack(opend,closed):
            if closed == opend == n:
                ans.append("".join(comp))
                return
            if closed < opend:
                comp.append(")")
                backtrack(opend,closed+1)
                comp.pop()
            if opend < n:
                comp.append("(")
                backtrack(opend+1,closed)
                comp.pop()

        backtrack(0,0)
        return ans
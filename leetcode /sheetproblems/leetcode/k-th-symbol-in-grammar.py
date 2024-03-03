class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def helper(n,curr,left,right):
            if n == 1:
                return curr
            mid = (left + right) // 2
            
            if k <= mid:
                return helper(n-1,curr,left,mid)
            return helper(n -1,0 if curr else 1,mid +1,right)
        return helper(n,0,1,2**(n-1))
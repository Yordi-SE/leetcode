class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(idx,sums,comp):
            if sums > n:
                return
            if len(comp) > k:
                return
            if sums == n and len(comp) == k:
                ans.append(comp[:])
                return
            for i in range(idx,10):
                comp.append(i)
                backtrack(i+1,sums + i,comp)
                comp.pop()
        backtrack(1,0,[])
        return ans
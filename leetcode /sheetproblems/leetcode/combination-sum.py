class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        seta = set()
        def backtrack(comp):  
            sums = sum(comp)       
            if  sums == target:
                c = tuple(sorted(comp))
                if c not in seta:
                    ans.append(comp[:])
                    seta.add(c)
                return
            if sums > target:
                return
            for i in range(len(candidates)):
                comp.append(candidates[i])
                backtrack(comp)
                comp.pop()
        # for i in range(1,len(candidates) + 1):
        backtrack([])
        return ans
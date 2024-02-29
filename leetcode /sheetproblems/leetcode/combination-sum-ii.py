class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        seta = set()
        candidates.sort()
        # print(candidates)
        def backtrack(sums,idx,comp):
            if sums > target:
                return
            if sums == target:
                # comps = tuple(comp[:])
                ans.append(comp[:])
                return
            for i in range(idx,len(candidates)):
                if idx != i and i > 0 and candidates[i] == candidates[i-1]:
                    continue
                comp.append(candidates[i])
                backtrack(sums + candidates[i],i + 1,comp)
                comp.pop()
        backtrack(0,0,[])
        return ans
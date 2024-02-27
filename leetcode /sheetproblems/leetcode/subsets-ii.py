class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seta = set()
        def backtrack(idx,k,comp):
            if len(comp) == k:
                c = tuple(sorted(comp))

                if c not in seta:
                    ans.append(comp[:])
                    seta.add(c)
                return
            for i in range(idx,len(nums)):
                comp.append(nums[i])
                backtrack(i+1,k,comp)
                comp.pop()
        for i in range(len(nums)+1):
            backtrack(0,i,[])
        return ans
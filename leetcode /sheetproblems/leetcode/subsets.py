class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx,k,comp):
            if len(comp) == k:
                ans.append(comp[:])
                return 
            for i in range(idx,len(nums)):
                comp.append(nums[i])
                # print(nums[i],comp,idx)
                backtrack(i + 1,k,comp)
                comp.pop()
        for i in range(len(nums)+1):
            backtrack(0,i,[])
        return ans
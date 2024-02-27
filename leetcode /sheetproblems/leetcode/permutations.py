class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        seta = set()
        def backtrack(comp):
            if len(comp) == n:
                ans.append(comp[:])
                return
            for i in range(len(nums)):
                if i not in seta:
                    comp.append(nums[i])
                    seta.add(i)
                    backtrack(comp)
                # if comp and i in seta:
                    comp.pop()
                    seta.discard(i)
        backtrack([])
        return ans
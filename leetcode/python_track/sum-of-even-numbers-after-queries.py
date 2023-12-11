class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums = 0
        res = []
        for i, u in enumerate(nums):
            if u % 2 == 0:
                sums += u
        for i in queries:
            val = nums[i[1]] + i[0]
            if val % 2 == 0:
                if nums[i[1]] % 2 == 0:
                    sums -= nums[i[1]]
                    sums += val
                else:
                    sums += val
            else:
                if nums[i[1]] % 2 == 0:
                    sums -= nums[i[1]]
            nums[i[1]] = val
            res.append(sums)
        return res
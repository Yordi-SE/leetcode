class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        sums = 0
        count = 0
        i = sums + 1
        pointer = 0
        while sums < n:
            if pointer < len(nums) and nums[pointer] <= i:
                sums += nums[pointer]
                pointer += 1
            if i > sums:
                count += 1
                sums += i
            i = sums + 1
        return count
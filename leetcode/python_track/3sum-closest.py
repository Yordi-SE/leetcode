class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mins = float("inf")
        for i in range(len(nums)):
            diff = target - nums[i]
            x = i + 1
            y = len(nums) - 1
            while x < y:
                diff2 = abs(diff - (nums[x] + nums[y]))
                if diff2 < mins:
                    sums = nums[x] + nums[y] + nums[i]
                    mins = diff2
                if (nums[x] + nums[y]) < diff:
                    x += 1
                elif (nums[x] + nums[y]) > diff:
                    y -= 1
                else:
                    break

        return sums

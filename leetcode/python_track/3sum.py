class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                x = i + 1
                y = len(nums) - 1
                while x < y:
                    sum = nums[x] + nums[y]  + nums[i]
                    if sum > 0:
                        y -= 1
                    elif sum < 0:
                        x += 1
                    elif sum == 0:
                        triplet = list([nums[x], nums[y], nums[i]])
                        triplet.sort()
                        x += 1
                        y -= 1
                        if triplet and triplet not in result:
                            result.append(triplet)

        return result

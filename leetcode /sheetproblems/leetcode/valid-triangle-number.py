class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)-1,-1,-1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] <= nums[i]:
                    left += 1
                elif nums[left] + nums[right] > nums[i]:
                    # print(nums[i],nums[right],nums[left])
                    # right -= 1
                    count += (right - left)
                    # break
                    right -= 1
                # else:
                #     print(nums[i],nums[right],nums[left])
                #     right -= 1
                #     left += 1
                #     count += 1
        return count
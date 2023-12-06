class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        perimeter = 0
        for i in range(len(nums) - 2):
            triangle = nums[i:i+3]
            # print( triangle)
            current_perimeter = sum(triangle)
            if triangle[0] + triangle[1] <= triangle[2]:
                continue
            elif triangle[2] + triangle[1] <= triangle[0]:
                continue
            elif triangle[0] + triangle[2] <= triangle[1]:
                continue
            if current_perimeter > perimeter:
                perimeter = current_perimeter
        return perimeter
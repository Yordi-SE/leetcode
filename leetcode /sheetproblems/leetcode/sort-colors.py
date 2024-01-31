class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        blue,red,white = 0,0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else:
                blue += 1
        for j in range(red):
            nums[j] = 0
        for j in range(white):
            nums[j + red] = 1
        for j in range(blue):
            nums[j + red + white] = 2
            
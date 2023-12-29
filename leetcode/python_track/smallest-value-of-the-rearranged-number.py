class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = list(str(num))

        for i in range(len(nums)):
            if num < 0:
                for j in range(1,len(nums) - 1):
                    if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
            else:
                for j in range(len(nums) - 1):
                    if nums[j] + nums[j + 1] > nums[j + 1] + nums[j]:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        # print(nums)
        nums = "".join(nums).lstrip("0")
        if num >0:
            counter = Counter(str(num))
            if '0' in counter :
                zeros = '0' * counter['0']
                # print(zeros)
                nums = nums[0] + zeros + nums[1:]
        # print(nums)
        return int(nums or 0)


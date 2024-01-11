class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seeker = 0
        placeholder = 0
        while seeker < len(nums):
            # print(seeker, placeholder)
            if nums[seeker] != val and nums[placeholder] == val:
                nums[placeholder], nums[seeker] = nums[seeker], nums[placeholder]
            if nums[placeholder] != val:
                placeholder += 1
            seeker += 1
        # print(nums)
        return placeholder
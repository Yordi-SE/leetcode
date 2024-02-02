class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        for i in self.nums:
            self.prefix.append(self.prefix[-1] + i)
        print(self.prefix)
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right + 1]
        return self.prefix[right + 1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
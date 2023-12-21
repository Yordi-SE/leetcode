class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        diff = []
        l,m,n = float('inf'), float('inf'), float('inf')
        for i in range(len(nums)):
            if nums[i] < l:
                l = nums[i]
            elif nums[i] < m and nums[i] > l:
                m = nums[i]
            elif nums[i] < n and nums[i] > m:
                n = nums[i]
        if l == float('inf') or m == float('inf') or n == float('inf'):
            return False
        elif l == m or m == n or n == l:
            return False
        return True

                
            
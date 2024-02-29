# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def divideAndConquer(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            
            mid = len(nums)//2
            curr = TreeNode(nums[mid])
            left = divideAndConquer(nums[:mid])
            right = divideAndConquer(nums[mid + 1:])
            curr.left = left
            curr.right = right
            return curr
        return divideAndConquer(nums)
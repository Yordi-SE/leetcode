# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        maxs = float('-inf')
        for i in range(len(nums)):
            if nums[i] >= maxs:
                mid = i
                maxs = nums[i]
        # print(nums)
        root = TreeNode(nums[mid])
        root.left = self.constructMaximumBinaryTree(nums[:mid])
        root.right = self.constructMaximumBinaryTree(nums[mid+1:])
        return root
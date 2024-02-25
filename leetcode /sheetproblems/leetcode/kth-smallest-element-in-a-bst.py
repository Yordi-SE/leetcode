# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = self.inOrder(root)
        return res[k-1]
    def inOrder(self,root):
        if root == None:
            return []
        val1 = self.inOrder(root.left)
        val2 = self.inOrder(root.right)
        return val1 + [root.val] + val2
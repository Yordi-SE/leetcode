# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = self.inOrder(root)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True
    def inOrder(self,root):
        if root == None:
            return []
        val = self.inOrder(root.left)
        val1 = self.inOrder(root.right)
        res = [root.val]
        return val + res + val1
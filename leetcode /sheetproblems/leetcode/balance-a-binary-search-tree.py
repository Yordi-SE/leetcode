# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        res = self.inorder(root)
        return self.helper(res)
    def inorder(self,root):
        if root == None:
            return []
        val1 = self.inorder(root.left)
        val2 = self.inorder(root.right)
        return val1 + [root.val] + val2
    def helper(self,res):
        if len(res) == 1:
            return TreeNode(res[-1])
        if len(res ) == 0:
            return None
        mid = len(res)//2
        root = TreeNode(res[mid])
        root.right = self.helper(res[mid+1:])
        root.left = self.helper(res[:mid])
        return root
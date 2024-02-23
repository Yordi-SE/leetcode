# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#     def __str__(self):
#         return "{}".format(self.val)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        val1 = self.search(root,p)
        val2 = self.search(root,q)
        set1 = set(val1)
        for i in range(len(val2)-1,-1,-1):
            if val2[i] in set1:
                return val2[i] 


    def search(self,root,p):
        if root == None:
            return []
        res = [root]
        val = []
        if p.val > root.val:
            val = self.search(root.right,p)
        elif p.val < root.val:
            val = self.search(root.left,p)
        return res + val

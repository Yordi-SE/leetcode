# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = self.helper(root)
        # print(res)
        maxs = float('-inf')
        for i in res:
            maxs = max(abs(i[0]-i[1]),maxs)
        return maxs
    def helper(self,root):
        if root == None:
            return []
        res = []
        val1 = self.helper(root.left)
        val2 = self.helper(root.right)
        if val1:
            for i in val1:
                i[0] = min(i[0],root.val)
                i[1] = max(i[1],root.val)
        else:
            val1 = [[root.val,root.val]]
        if val2:
            for i in val2:
                i[0] = min(i[0],root.val)
                i[1] = max(i[1],root.val)
        else:
            val2 = [[root.val,root.val]]
        # print(val1)
        # print(val2)

        return val1 + val2
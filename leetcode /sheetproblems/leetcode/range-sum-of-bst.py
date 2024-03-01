# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0
        if low <= root.val <= high:
            val = root.val 
            # print(root.val)
        else:
            val = 0
        if root.val <= low:
            val += self.rangeSumBST(root.right,low,high)
        if root.val >= high:
            val += self.rangeSumBST(root.left,low,high)
        if low < root.val < high:
            val += self.rangeSumBST(root.left,low,high)
            val += self.rangeSumBST(root.right,low,high)
        return val
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        right = self.postOrder(root.right,"right")
        # print(right)
        left = self.inOrder(root.left,"left")
        # print(left)
        if len(left) != len(right):
            return False
        for i in range(len(left)):
            if left[i][0] == right[i][0] and left[i][1] == right[i][1]:
                # print(left[i])
                # print(right[i])
                return False
            elif left[i][0] != right[i][0]:
                return False
        return True
    def inOrder(self,root,direction):
        if root == None:
            return []
        
        val1 = self.inOrder(root.left,"left")
        val2 = self.inOrder(root.right,"right")
        return val1 + [(root.val,direction)] + val2
    def postOrder(self,root,direction):
        if root == None:
            return []
        
        val1 = self.postOrder(root.left,"left")
        val2 = self.postOrder(root.right,"right")
        return val2 + [(root.val,direction)] + val1
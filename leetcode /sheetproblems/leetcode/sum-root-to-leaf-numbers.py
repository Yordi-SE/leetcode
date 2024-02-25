# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        val = list(map(int,self.helper(root).split(",")))
        return sum(val)
    def helper(self,root):
        if root == None:
            return ""
        res = str(root.val)
        val1 = self.helper(root.left)
        if val1 != "":
            val1 = val1.split(",")
            for i in range(len(val1)):
                val1[i] = res + val1[i]
            val1 = ",".join(val1)

        val2 = self.helper(root.right)
        if val2 != "":
            val2 = val2.split(",")
            for i in range(len(val2)):
                val2[i] = res + val2[i]
            val2 = ",".join(val2)
        if val1 == "" and val2 != "":
            return val2
        elif val1 != "" and val2 == "":
            return val1
        elif val1 == "" and val2 == "":
            return res

        return val1 + "," + val2

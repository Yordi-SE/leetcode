# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = self.search(root)
        list1 = sorted(res.items(),key=lambda x:x[1],reverse=True)
        res = []
        for i in range(len(list1)):
            if list1[i][1] == list1[0][1]:
                res.append(list1[i][0])
        return res
    def search(self,root):
        if root == None:
            return defaultdict(int)
        res = defaultdict(int) 
        res[root.val] += 1
        val1 = self.search(root.right)
        val2 = self.search(root.left)
        for i in val1:
            res[i] += val1[i]
        for i in val2:
            res[i] += val2[i]
        return res
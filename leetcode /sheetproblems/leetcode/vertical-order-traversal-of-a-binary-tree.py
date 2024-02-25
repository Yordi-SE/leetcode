# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res =self.helper(root,0,0)
        res.sort(key=lambda x:(x[1],x[2],x[0]))
        hashmap = {}
        for i in range(len(res)):
            if res[i][1] in hashmap:
                hashmap[res[i][1]].append(res[i][0])
            else:
                hashmap[res[i][1]] = [res[i][0]]
        # print(res)
        res2 = []
        for i in range(len(res)):
            if res[i][1] in hashmap:
                res2.append(hashmap[res[i][1]])
                del hashmap[res[i][1]]
        return (res2)
    def helper(self,root,column,row):
        if root == None:
            return []
        res = [[root.val,column,row]]
        val1 = self.helper(root.right,column+1,row+1)
        val2 = self.helper(root.left,column-1,row+1)
        return res + val2 + val1

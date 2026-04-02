# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root, value, res):
            if not root:
                return res
            if root.val == value:
                return res
            res.append([root.val,root])
            if root.val < value:
                dfs(root.right, value, res)
            else:
                dfs(root.left, value, res)
            return res
        
        res1 = dfs(root, p.val, [])
        res2 = dfs(root, q.val, [])
        obj = next((item[1] for item in res2 if item[0] == p.val), None)
        if obj:
            return obj
        obj = next((item[1] for item in res1 if item[0] == q.val), None)
        if obj:
            return obj
        i=0
        while i < len(res1) and i < len(res2) and res1[i][0] == res2[i][0]:
            i += 1
        return res1[i-1][1]



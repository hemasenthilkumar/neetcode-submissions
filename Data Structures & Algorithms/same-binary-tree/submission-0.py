# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        verdict = True

        def dfs(p, q):
            nonlocal verdict
            condition = (p is None and q is None) or (p is not None and q is not None)
            if not condition:
                verdict = False
                return
            if not p and not q:
                return 
            if p.val != q.val:
                verdict = False
            dfs(p.left, q.left)
            dfs(p.right, q.right)
        
        dfs(p,q)
        return verdict

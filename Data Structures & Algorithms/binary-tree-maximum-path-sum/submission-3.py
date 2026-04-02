# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maxSum = float('-inf')
        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0
            tsl = dfs(root.left)
            tsr = dfs(root.right) 
            tsl = max(tsl, 0)
            tsr = max(tsr, 0)
            maxSum = max(tsl + tsr + root.val, maxSum)
            return max(tsl + root.val, tsr+root.val)
    
        dfs(root)
        return maxSum
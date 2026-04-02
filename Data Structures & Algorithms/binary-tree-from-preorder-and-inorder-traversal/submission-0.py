# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    
            if not preorder or not inorder:
                return 
            root = preorder[0]
            r = TreeNode(root)
            root_place = inorder.index(root)
            r.left = self.buildTree(preorder[1:root_place+1], inorder[:root_place])
            r.right = self.buildTree(preorder[root_place+1:], inorder[root_place+1:])
            return r

    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr=  root

        while curr or stack:
            # go left
            while curr:
                stack.append(curr)
                curr = curr.left 
            # once far left is reached.
            # get the last element
            curr = stack.pop()
            # process it
            n += 1
            if n == k:
                return curr.val
            # process done
            # then if not satisfied, go to the right node
            curr = curr.right





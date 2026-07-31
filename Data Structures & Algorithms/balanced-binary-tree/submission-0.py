# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        gc = True
        def dfs(node, h):
            nonlocal gc
            if not node:
                return h
            
            lh = dfs(node.left, 1+h)
            rh = dfs(node.right, 1+h)
            if abs(lh-rh) > 1:
                gc = False
            return max(lh, rh)
            

        h = dfs(root, 1)
        return gc
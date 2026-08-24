# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return [0, 0]
            l, lo = dfs(node.left)
            r, ro = dfs(node.right)
            return node.val + lo + ro, max(l, lo) + max(r, ro) 

        return max(dfs(root))
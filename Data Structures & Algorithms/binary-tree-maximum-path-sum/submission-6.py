# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        gmax = -float("inf")
        def dfs(node):

            nonlocal gmax
            l = dfs(node.left) if node.left else 0
            l = max(l, 0)
            r = dfs(node.right) if node.right else 0
            r = max(r, 0)
            # print(l, r, node.val, gmax)
            gmax = max(gmax, node.val+l+r)
            return max(l+node.val, r+node.val)

        dfs(root)
        return gmax
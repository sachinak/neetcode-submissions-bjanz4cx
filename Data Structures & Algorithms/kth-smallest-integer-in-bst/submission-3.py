# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = None
        def dfs(node, k):
            nonlocal res
            if node.left:
                dfs(node.left, k)
            k[0]-=1
            if k[0] == 0:
                res= node.val
            if node.right:
                dfs(node.right, k)

        dfs(root, [k])
        return res
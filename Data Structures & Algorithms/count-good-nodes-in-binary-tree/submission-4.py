# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = []
        curr = [root.val]
        maxv = root.val
        def dfs(root, maxv):
            if not root:
                return
            maxv = max(maxv, root.val)
            if root.val >= maxv:
                res.append(root.val)
            # if root.left: 
            dfs(root.left, maxv)
            # if root.right:
            dfs(root.right, maxv)
            
        
        
        dfs(root, maxv)
        
        return len(res)
        
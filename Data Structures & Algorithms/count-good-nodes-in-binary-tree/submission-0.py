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
        def dfs(root):
            curr.append(root.val)
            if root.val == max(curr):
                res.append(root.val)
            if root.left: 
                dfs(root.left)
            if root.right:
                dfs(root.right)
            curr.pop()
        
        
        dfs(root)
        
        return len(res)
        
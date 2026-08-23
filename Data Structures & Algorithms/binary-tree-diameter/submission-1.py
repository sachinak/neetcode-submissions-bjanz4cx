# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        gc = 0
        def tre(node):
            nonlocal gc
            if not node:
                return 0
            
            l = 1+tre(node.left) if node.left else 0
            r = 1+tre(node.right) if node.right else 0
            gc = max(gc, l+r)

            return max(l, r)
        
        tre(root)
        return gc
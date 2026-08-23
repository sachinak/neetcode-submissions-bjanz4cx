# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def tre(node):
            if not node:
                return None
            l = node.left
            
            node.left = tre(node.right)
            node.right = tre(l)
            return node
            
        return tre(root)
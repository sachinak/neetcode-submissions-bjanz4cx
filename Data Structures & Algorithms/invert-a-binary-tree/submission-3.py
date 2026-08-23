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
            node.left, node.right = tre(node.right), tre(node.left)
            return node
        return tre(root)
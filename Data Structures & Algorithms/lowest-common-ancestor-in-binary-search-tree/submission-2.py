# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def tre(node):
            
            if p.val == node.val or q.val == node.val:
                return node
            elif p.val > node.val and q.val > node.val:
                return tre(node.right)
            elif p.val < node.val and q.val < node.val:
                return tre(node.left)
            return node
            
        return tre(root)
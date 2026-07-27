# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def traverse(root):
            if p.val == root.val or q.val ==root:
                return root
            elif p.val > root.val and q.val > root.val:
                return traverse(root.right)
            elif p.val < root.val and q.val < root.val:
                return traverse(root.left)
            else:
                return root
        
        return traverse(root)
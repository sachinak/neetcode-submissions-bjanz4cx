# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def tre(node):
            if not node:
                return
            tre(node.left)
            res.append(node.val)
            tre(node.right)
        tre(root)
        return res
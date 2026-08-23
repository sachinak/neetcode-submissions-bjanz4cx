# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def tre(node, h, flag):
            if not node:
                return h
            l = tre(node.left, 1+h, flag)
            r = tre(node.right, 1+h, flag)
            if abs(l-r) > 1:
                flag[0] = False
            return max(l, r)

        flag = [True]
        tre(root, 0, flag)
        return flag[0]
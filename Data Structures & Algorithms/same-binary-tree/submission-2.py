# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def pre(node, arr):
            if not node:
                arr.append(None)
                return
            arr.append(node.val)
            pre(node.left, arr)
            pre(node.right, arr)
        

        res1, res2 = [], []
        pre(p, res1)
        pre(q, res2)
        return res1 == res2
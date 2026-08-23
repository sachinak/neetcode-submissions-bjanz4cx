# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        def pre(node, pathMax, res):
            if not node:
                return
            pathMax = max(pathMax, node.val)
            if node.val == pathMax:
                res[0]+=1

            pre(node.left, pathMax, res)
            pre(node.right, pathMax, res)
        
        pre(root, root.val, res)
        return res[0]
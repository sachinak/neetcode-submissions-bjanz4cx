# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        q = [root]
        res = []

        while q:
            item = q.pop(0)
           
            res.append(item.val)
            if item.left: q.append(item.left)
            if item.right: q.append(item.right)
        
        return sorted(res)[k-1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        def dfs(node, cntr):
            if node.left:
                dfs(node.left,cntr)
            cntr[0]-=1
            if cntr[0] == 0:
                cntr.append(node.val)
            if node.right:
                dfs(node.right, cntr)

        cntr = [k]
        dfs(root, cntr)
        return cntr[1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        

        def dfs(node):
            if not node.left and not node.right and node.val == target:
                return True
            
            lr = False
            if not node.left:
                lr = True
            elif node.left and dfs(node.left):
                node.left = None
                lr = True
            rr = False
            if not node.right:
                rr = True
            elif node.right and dfs(node.right):
                node.right = None
                rr = True
            if lr and rr and node.val == target:
                return True
            return False
        
        if dfs(root):
            return None
        return root
            
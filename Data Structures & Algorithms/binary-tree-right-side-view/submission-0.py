# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []


        d = {}
        q = [[root, 0]]

        while q:
            node, level = q.pop(0)
            if d.get(level):
                d[level].append(node.val)
            else:
                d[level] = [node.val]
            if node.left: q.append((node.left, level+1))
            if node.right: q.append((node.right, level+1))
        
        res = []
        
        for items in d:
            
            res.append(d[items][-1])
        return res

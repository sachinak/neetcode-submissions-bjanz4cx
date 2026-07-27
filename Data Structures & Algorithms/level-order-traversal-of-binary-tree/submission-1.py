# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        q = [(root, 0)]
        d = {}
        while q:
            nod = q.pop(0)
            if d.get(nod[1]):
                d[nod[1]].append(nod[0].val)
            else:
                d[nod[1]] = [nod[0].val]
            
            if nod[0].left: q.append((nod[0].left, nod[1]+1))
            if nod[0].right: q.append((nod[0].right, nod[1]+1))
        
        k = d.values()
        return (list(k))
        return res
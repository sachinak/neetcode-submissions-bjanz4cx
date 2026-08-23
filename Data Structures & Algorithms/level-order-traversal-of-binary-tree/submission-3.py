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
        q = deque()
        q.append([root, 0])
        res = defaultdict(list)
        while q:
            node, d = q.popleft()
            
            res[d].append(node.val)
            if node.left: q.append([node.left, d+1])
            if node.right: q.append([node.right, d+1])
        return [res[key] for key in res]
            

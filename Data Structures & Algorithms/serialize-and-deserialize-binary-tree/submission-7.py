# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def pre(self, node, res):
        if not node:
            res.append("N")
            return
        res.append(str(node.val))
        self.pre(node.left, res)
        self.pre(node.right, res)
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        self.pre(root, res)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        res = data.split(",")
        if not res:
            return None
        self.idx = 0
        
        def pre(res):
            v = res[self.idx]
            self.idx+=1
            if v == 'N':
                return None
            
            node = TreeNode(int(v))
            node.left = pre(res)
            node.right = pre(res)
            return node
            

        return pre(res)
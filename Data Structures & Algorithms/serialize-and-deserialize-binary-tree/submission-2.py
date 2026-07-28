# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        
        def pre(node):
            if not node:
                arr.append("N")
                return
            arr.append(str(node.val))
            pre(node.left)
            
            pre(node.right)
        pre(root)

        
        s = "|".join(arr)
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pre = data.split("|")
        self.idx= 0
        def dfs():
            if pre[self.idx] == 'N':
                self.idx+=1
                return None
            # print(int(pre[sidx]),idx)
            node = TreeNode(int(pre[self.idx]))
            self.idx+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
        
        
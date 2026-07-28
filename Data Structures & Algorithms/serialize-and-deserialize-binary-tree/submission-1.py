# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.pres=""
        
        def pre(node):
            if not node:
                self.pres+="N|"
                return
            self.pres+=str(node.val) + "|"
            pre(node.left)
            
            pre(node.right)
        pre(root)

        
        s= self.pres
        print(s)
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pre = data.split("|")[:-1]
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
        
        
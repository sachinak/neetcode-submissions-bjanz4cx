# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        msum = -float('inf')
        def tre(root):
            if not root: return 0
            
            lsum = tre(root.left) if root.left else 0
            rsum = tre(root.right) if root.right else 0
            val = root.val
            
            
            ll = val + lsum
            rl = val + rsum
            tl = val + lsum + rsum

            maxsum = max(val, ll, rl,tl)
            nonlocal msum
            msum = max(msum, maxsum)
            # print(root.val, lsum, rsum, maxsum, msum)
            return max(ll, rl, val)

        t = tre(root)
        return msum
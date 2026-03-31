# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxpath = float("-inf")

        def dfs(node):
            if not node:
                return 0
            
            leftmax = max(0,dfs(node.left))
            rightmax = max(0,dfs(node.right))

            self.maxpath = max(self.maxpath,node.val+leftmax+rightmax)

            return node.val + max(leftmax,rightmax)

        
        dfs(root)
        return self.maxpath
        
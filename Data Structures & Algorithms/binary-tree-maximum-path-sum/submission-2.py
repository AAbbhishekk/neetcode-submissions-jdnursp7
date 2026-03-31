# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxi=float("-inf")

        def maxsum(node):
            if not node:
                return 0
            
            leftmax = max(0,maxsum(node.left))
            rightmax = max(0,maxsum(node.right))

            self.maxi = max(self.maxi,node.val+leftmax+rightmax)

            return node.val + max(leftmax,rightmax)


        maxsum(root)
        return self.maxi
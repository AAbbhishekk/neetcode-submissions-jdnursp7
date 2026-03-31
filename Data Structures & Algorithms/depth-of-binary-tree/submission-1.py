# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        from collections import deque

        tree = deque([root])
        count = 0

        while tree:
            for i in range(len(tree)):
                node = tree.popleft()
            
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            count = count + 1

        return count

        
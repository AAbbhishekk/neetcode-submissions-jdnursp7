# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []

        tree = deque([root])

        res = []
        while tree:
            level = len(tree)
            for i in range(level):
                node = tree.popleft()
                if i ==level -1:
                    res.append(node.val)
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)

        return res        
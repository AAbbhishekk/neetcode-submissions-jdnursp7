# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []
        
        tree = deque([root])

        res = []

        while tree:
            temp = []
            for i in range(len(tree)):
                node = tree.popleft()
                
                temp.append(node.val)
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)

            res.append(temp)

        return res
        
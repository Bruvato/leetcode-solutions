# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        if not root.left and not root.right:
            return root
        

        s = []
        s.append(root)

        while s:
            node = s.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)

        
        return root

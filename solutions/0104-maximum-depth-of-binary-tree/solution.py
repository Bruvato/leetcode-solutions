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
        if not root.left and not root.right:
            return 1
        
        res = 0

        s = deque()
        s.append(root)

        while s:
            for i in range(len(s)):
                node = s.popleft()
                if node.left:
                    s.append(node.left)
                if node.right:
                    s.append(node.right)
            res += 1

        return res

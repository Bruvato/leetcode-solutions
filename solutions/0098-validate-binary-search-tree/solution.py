# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not root.left and not root.right:
            return True

        q = deque()
        q.append((root, float("-inf"), float("inf")))

        while q:
            node, l, r = q.pop()

            if not (l < node.val < r):
                return False
            
            if node.left:
                q.append((node.left, l, node.val))
            if node.right:
                q.append((node.right, node.val, r))


        return True

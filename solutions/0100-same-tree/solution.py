# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False

        s = []

        s.append((p, q))

        while s:
            n, m = s.pop()
            print(n,m)

            if n.val != m.val:
                return False
            if (n.left == None) != (m.left == None):
                return False
            if (n.right == None) != (m.right == None):
                return False
            
            if n.left and m.left:
                s.append((n.left, m.left))
            if n.right and m.right:
                s.append((n.right, m.right))
        
        return True

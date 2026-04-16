# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        hm = {None: (0, 0)}
        s = []
        s.append(root)
        
        while s:
            peek = s[-1]

            if peek.left and peek.left not in hm:
                s.append(peek.left)
            elif peek.right and peek.right not in hm:
                s.append(peek.right)
            else:
                node = s.pop()

                lh, ld = hm[node.left]
                rh, rd = hm[node.right]

                hm[node] = 1 + max(lh, rh), max(lh + rh, ld, rd)

        return hm[root][1]
            
            


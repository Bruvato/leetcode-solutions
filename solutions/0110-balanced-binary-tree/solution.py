# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        hm = {None: 0}

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

                lh = hm[node.left]
                rh = hm[node.right]

                if abs(lh - rh) > 1:
                    return False
                
                hm[node] = 1 + max(lh, rh)
            
        return True

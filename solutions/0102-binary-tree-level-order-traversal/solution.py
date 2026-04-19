# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        if not root.left and not root.right:
            return [[root.val]]
        
        res = []
        
        s = []

        s.append((root, 0))

        while s:
            node, depth = s.pop()
            n = len(res)

            if n == depth:
                res.append([])
            
            res[depth].append(node.val)

            if node.right:
                s.append((node.right, depth + 1))
            if node.left:
                s.append((node.left, depth + 1))


        return res

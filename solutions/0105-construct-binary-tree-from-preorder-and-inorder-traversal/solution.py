# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hm = {}

        n = len(inorder)

        for i in range(n):
            hm[inorder[i]] = i

        self.pre_idx = 0

        def dfs(l, r):
            if l > r:
                return None
            
            root = TreeNode(preorder[self.pre_idx])
            mid = hm[preorder[self.pre_idx]]
            self.pre_idx += 1
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)

            return root
        
        return dfs(0, n - 1)

        

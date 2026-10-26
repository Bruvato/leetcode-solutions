# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {root: None}

        def dfs(node):
            if not node:
                return node
            
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)
        
        dfs(root)


        q = deque([target])
        visited = {target}
        level = 0
        res = []

        while q and level <= k:
            n = len(q)

            for i in range(n):

                node = q.popleft()
                visited.add(node)
                if level == k:
                    res.append(node.val)

                if node.left and node.left not in visited:
                    q.append(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                if parent[node] and parent[node] not in visited:
                    q.append(parent[node])
            
            level += 1

        return res


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        
        n = len(grid)

        if grid[n - 1][n - 1] == 1 or grid[0][0] == 1:
            return -1
        
        dirs = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        seen = {(0, 0)}
        q = deque([((0, 0), 1)])
        
        while q:
            node = q.popleft()
            coord, l = node

            if coord == (n - 1, n - 1):
                return l
            
            r, c = coord

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in seen and grid[nr][nc] != 1:
                    seen.add((nr, nc))
                    q.append(((nr, nc), l + 1))

        return -1

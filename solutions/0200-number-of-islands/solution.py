class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        res = 0

        def bfs(coord):

            q = deque([coord])

            while q:
                r, c = q.popleft()
                grid[r][c] = 'x'

                for d in dirs:
                    nr = r + d[0]
                    nc = c + d[1]

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        grid[nr][nc] = 'x'
                        q.append((nr, nc))

        for r in range(m):
            for c in range(n):
                cell = grid[r][c]

                if cell == 'x' or cell == '0':
                    continue

                res += 1
                bfs((r, c))

        return res

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        q = deque([])
        rotten = 0
        oranges = 0
        t = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue
                
                if grid[r][c] == 2:
                    q.append((r, c))
                    rotten += 1
                
                oranges += 1
        
        if rotten == oranges:
            return 0
        
        while q:
            t += 1
            for i in range(len(q)):
                node = q.popleft()

                r, c = node

                for dr, dc in dirs:
                    nr, nc = dr + r, dc + c

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten += 1
                        q.append((nr, nc))
                        if rotten == oranges:
                            return t
        
        return -1

        

        return -1

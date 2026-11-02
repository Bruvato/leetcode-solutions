class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(coord, seen):
            seen.add(coord)
            r, c = coord

            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                    seen.add((nr, nc))
                    dfs((nr, nc), seen)
            
            return seen

        pacific = set()
        atlantic = set()
        for r in range(m):
            dfs((r, 0), pacific)
            dfs((r, n - 1), atlantic)
        for c in range(n):
            dfs((0, c), pacific)
            dfs((m - 1, c), atlantic)

        return list(pacific & atlantic)

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        res = []

        for y in range(1, n - 1):
            row = []
            for x in range(1, n - 1):

                row.append(max(
                    grid[y-1][x-1],
                    grid[y-1][x],
                    grid[y-1][x+1],
                    grid[y][x-1],
                    grid[y][x],
                    grid[y][x+1],
                    grid[y+1][x-1],
                    grid[y+1][x],
                    grid[y+1][x+1]
                ))
            res.append(row)
        
        return res

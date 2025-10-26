class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        

        m, n = len(mat), len(mat[0])
        x, y = 0, 0
        res = []

        for i in range(m * n):
            res.append(mat[y][x])

            # up right
            if (x + y) % 2 == 0:
                if x == n - 1:
                    y += 1
                elif y == 0:
                    x += 1
                else:
                    y -= 1
                    x += 1
            # down left
            else:
                if y == m - 1:
                    x += 1
                elif x == 0:
                    y += 1
                else:
                    y += 1
                    x -= 1

        return res



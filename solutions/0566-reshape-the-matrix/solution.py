class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        

        m = len(mat)
        n = len(mat[0])


        if m * n != r * c:
            return mat

        arr = []
        i = 0

        for y in range(0, m):
            for x in range(0, n):
                arr.append(mat[y][x])

        res = []
        for y in range(r):
            row = []
            for x in range(c):
                row.append(arr[i])
                i += 1
            res.append(row)

        return res

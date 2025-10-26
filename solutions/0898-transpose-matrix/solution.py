class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        res = []

        for y in range(len(matrix[0])):
            row = []
            for x in range(len(matrix)):
                row.append(matrix[x][y])
            res.append(row)

        return res

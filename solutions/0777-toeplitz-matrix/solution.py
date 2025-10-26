class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m = len(matrix)
        n = len(matrix[0])

        for y in range(1, m):
            for x in range(1, n):
                if matrix[y][x] != matrix[y - 1][x - 1]:
                    return False
        
        return True

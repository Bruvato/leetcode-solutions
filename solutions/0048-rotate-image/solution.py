class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        top = 0
        bottom = n - 1

        while top < bottom:
            temp = matrix[top]
            matrix[top] = matrix[bottom]
            matrix[bottom] = temp
            top += 1
            bottom -= 1
        

        for i in range(0, n - 1):
            for j in range(min(i + 1, n - 1), n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        



        

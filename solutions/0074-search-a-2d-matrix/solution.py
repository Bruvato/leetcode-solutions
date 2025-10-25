class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        u = 0
        d = m - 1

        while u <= d:
            mid = (u + d) // 2
            
            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                l = 0
                r = n - 1
                while l <= r:
                    mid2 = (l + r) // 2
                    print(mid2)
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] < target:
                        l = mid2 + 1
                    else:
                        r = mid2 - 1

                return False
            elif target < matrix[mid][0]:
                d = mid - 1
            else:
                u = mid + 1
        
        return False


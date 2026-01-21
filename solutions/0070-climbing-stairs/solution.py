class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        hm = {}
        hm[1] = 1
        hm[2] = 2

        for i in range(3, n + 1):
            hm[i] = hm[i - 1] + hm[i - 2]
        
        return hm[n]

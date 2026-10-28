class Solution:
    def climbStairs(self, n: int) -> int:
        # self.hm = {
        #     1: 1,
        #     2: 2
        # }

        # def help(n):
        #     if n in self.hm:
        #         return self.hm[n]
            
        #     res = help(n - 1) + help (n - 2)
        #     self.hm[n] = res

        #     return res
        
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n - 1]
        # return help(n)

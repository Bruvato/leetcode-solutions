class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        def dfs(curr: str, open: int, close: int):
            if len(curr) == 2 * n:
                self.res.append(curr)
                return
            
            if close > open:
                return
            
            if open < n:
                dfs(curr + "(", open + 1, close)
            if close < open:
                dfs(curr + ")", open, close + 1)
        
        dfs("", 0, 0)

        return self.res

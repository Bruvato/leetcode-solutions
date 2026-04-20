class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.res = []

        n = len(digits)

        hm = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def dfs(i: int, curr: str):
            if i == n:
                self.res.append(curr)
                return
            letters = hm[digits[i]]
            for c in letters:
                dfs(i + 1, curr + c)
        
        dfs(0, "")

        return self.res

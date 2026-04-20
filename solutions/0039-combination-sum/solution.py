class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        self.res = []

        def dfs(i, curr, total):
            if total == target:
                self.res.append(curr.copy())
                return

            if i >= n or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return self.res

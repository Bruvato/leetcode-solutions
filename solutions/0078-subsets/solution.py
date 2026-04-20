class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.res = []

        def dfs(i, subset):
            if i >= n:
                self.res.append(subset.copy())
                return
            
            dfs(i + 1, subset.copy())

            subset.append(nums[i])

            dfs(i + 1, subset.copy())
        

        dfs(0, [])

        return self.res

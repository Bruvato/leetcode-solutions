class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.res = []


        def dfs(curr, seen):
            if len(curr) == n:
                self.res.append(curr.copy())
                return
            
            for i in range(n):
                if not seen[i]:
                    curr.append(nums[i])
                    seen[i] = True
                    dfs(curr, seen)
                    curr.pop()
                    seen[i] = False
        
        dfs([], [False] * n)
        return self.res

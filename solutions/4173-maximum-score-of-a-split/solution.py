class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        n = len(nums)

        pre = [0] * n
        suf = [0] * n
        pre[0] = nums[0]
        suf[n - 1] = nums[n - 1]

        
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]

        for i in range(n - 2, -1, -1):
            suf[i]  = min(nums[i], suf[i + 1])
        

        res = pre[0] - suf[1]

        for i in range(0, n - 1):
            res = max(res, pre[i] - suf[i + 1])

        return res


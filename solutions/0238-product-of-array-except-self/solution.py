class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [nums[0]] * n
        suffix = [nums[n - 1]] * n
        res = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        for i in range(n):
            l = prefix[i - 1] if i > 0 else 1
            r = suffix[i + 1] if i < n -1 else 1
            res[i] = l * r
        
        return res


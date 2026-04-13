class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 1:
            return nums[0]

        
        # -2, 1, -3, 4, -1, 2, 1, -5, 4
        res = nums[0]
        l = 0
        curr = 0


        for r in range(n):
            if curr < 0:
                l = r
                curr = 0
            
            curr += nums[r]
            res = max(res, curr)
        

        return res
            


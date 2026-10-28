class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])

        # self.hm = {
        #     0: nums[0],
        #     1: max(nums[0], nums[1])
        # }

        # [2,7,9,3,1]
        # [2,7,11,11,12]

        # def help(i):
        #     if i in self.hm:
        #         return self.hm[i]
            
        #     res = max(nums[i] + help(i - 2), help(i - 1))
        #     self.hm[i] = res
        #     return res
        nums[1] = max(nums[0], nums[1])

        for i in range(2, n):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        
        # return help(n - 1)
        return nums[n - 1]


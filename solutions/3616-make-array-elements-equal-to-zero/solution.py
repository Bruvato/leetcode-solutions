class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        count = 0
        n = len(nums)
        l = 0
        r = sum(nums)

        for i in range(n):
            l += nums[i]
            r -= nums[i]

            if nums[i] != 0:
                continue
            
            if l == r:
                count += 2
            
            if abs(l - r) == 1:
                count += 1

        return count



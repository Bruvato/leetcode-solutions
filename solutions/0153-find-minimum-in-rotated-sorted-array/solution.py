class Solution:
    def findMin(self, nums: list[int]) -> int:
        res = nums[0]

        n = len(nums)

        l = 0
        r = n -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[0]:
                l = mid + 1
            elif nums[mid] <= nums[0]:
                res = min(res, nums[mid])
                r = mid - 1
                res = min(res, nums[r])

        
        return res

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            print(l, mid)
            if nums[l] <= nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            
        return nums[l]
            


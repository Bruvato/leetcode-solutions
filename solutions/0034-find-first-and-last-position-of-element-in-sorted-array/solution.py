class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1

        def binSearch(l, r, left):
            i = -1
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    i = mid
                    if left:
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
            
        
        return [binSearch(l, r, True), binSearch(l, r, False)]

        



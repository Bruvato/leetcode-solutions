class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        n = len(arr)
        l = 0
        r = n -1

        while l <= r:
            mid = (l + r) // 2

            ln = max(0, mid - 1)
            rn = min(n - 1, mid + 1)

            if arr[ln] <= arr[mid] >= arr[rn]:
                return mid
            elif arr[ln] > arr[mid]:
                r = mid - 1
            elif arr[rn] > arr[mid]:
                l = mid + 1
        
        


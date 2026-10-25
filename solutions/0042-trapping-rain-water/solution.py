class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        l = 0
        r = n - 1

        maxl = height[l]
        maxr = height[r]

        res = 0

        while l < r:
            maxl = max(maxl, height[l])
            maxr = max(maxr, height[r])

            if height[l] <= height[r]:
                res += max(0, min(maxl, maxr) - height[l])
                l += 1
            else:
                res += max(0, min(maxl, maxr) - height[r])
                r -= 1

        return res

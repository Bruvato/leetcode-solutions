class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_water = 0

        while l < r:
            if height[l] <= height[r]:
                water = (r - l) * height[l]
                l += 1
            elif height[l] > height[r]:
                water = (r - l) * height[r]
                r -= 1
            
            if water > max_water:
                max_water = water
        
        return max_water

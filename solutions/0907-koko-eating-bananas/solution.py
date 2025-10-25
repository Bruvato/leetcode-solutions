import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        n = len(piles)

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(p/k)
            
            if hrs > h:
                l = k + 1
            else:
                res = min(k, res)
                r = k - 1
        
        return res
        

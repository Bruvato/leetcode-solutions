class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            hrs = 0
            for p in piles:
                hrs += math.ceil(p / k)
            
            if hrs > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        
        return res


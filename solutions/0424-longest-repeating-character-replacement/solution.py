class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hm = {}
        l = 0
        res = 0
        maxf = 0

        for r in range(n):
            hm[s[r]] = hm.get(s[r], 0) + 1
            if hm[s[r]] > maxf:
                maxf = hm[s[r]]
            
            while (r - l + 1) - maxf > k:
                hm[s[l]] -= 1
                l += 1
            
            if r - l + 1 > res:
                res = r - l + 1

        return res

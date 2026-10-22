class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0
        
        if n == 1:
            return 1

        
        # abcabcbb
        # l
        #  r

        res = 1
        
        l, r = 0, 0
        hm = {}
        while r < n - 1:
            hm[s[r]] = r
            r += 1

            if s[r] in hm:
                res = max(res, r - l)
                l = hm[s[r]] + 1
                r = l
                hm.clear()
        
        if s[r] not in hm:
            res = max(res, r - l + 1)

        return res


        

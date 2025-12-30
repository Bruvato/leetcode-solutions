class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        l = 0

        mp = {}
        res = 0

        for r in range(n):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)

            mp[s[r]] = r
            res = max(res, r - l + 1)

        return res

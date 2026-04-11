class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0

        letters = [-1] * 128

        for r in range(len(s)):
            if letters[ord(s[r])] >= l:
                l = letters[ord(s[r])] + 1
            
            res = max(res, r - l + 1)
            letters[ord(s[r])] = r

        return res


        

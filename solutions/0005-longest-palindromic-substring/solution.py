class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # b a b a d
        # L.  R

        # c b b d
        # L.    R


        # abbccccca
        # L
        #  R

        # aba

        # abba


        n = len(s)

        if n == 1:
            return s[0]

        
        start = 0
        end = 0
        max_len = 1

        for i in range(n):
            l = i
            r = i + 1

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    start, end = l, r
                l -= 1
                r += 1
        
        for i in range(n):
            l = i - 1
            r = i + 1
            sub = s[i]

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > max_len:
                    max_len = r - l + 1
                    start, end, = l, r
                    
                l -= 1
                r += 1

        return s[start:end + 1]

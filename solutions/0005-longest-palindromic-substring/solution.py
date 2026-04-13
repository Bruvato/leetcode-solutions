class Solution:
    def longestPalindrome(self, s: str) -> str:
        # a

        # aa

        # ba

        #bab

        #bac

        #cadbbd

        n = len(s)
        resLen = 0
        res = ""

        for i in range(n):
            l = i
            r = i

            while 0 <= l and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]

                l -= 1
                r += 1
            
            l = i
            r = i + 1

            while 0 <= l and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]

                l -= 1
                r += 1

        
        return res        

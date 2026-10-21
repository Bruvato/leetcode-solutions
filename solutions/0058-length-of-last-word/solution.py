class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        res = 0
        n = len(s)
        i = n - 1

        while i >= 0:
            if s[i] == ' ':
                if res == 0:
                    i -= 1
                    continue
                else:
                    break
            else:
                i -= 1
                res += 1
            
        
        return res

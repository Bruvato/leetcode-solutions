import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = re.sub(r'[^a-z0-9]', '', s.lower())
        
        l = 0
        r = len(valid) - 1

        while l < r:
            if (valid[l] != valid[r]):
                return False
            l += 1
            r -= 1
        
        return True

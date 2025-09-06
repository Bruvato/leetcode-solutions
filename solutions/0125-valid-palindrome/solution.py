import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = re.sub(r'[^a-z0-9]', '', s.lower())
        return valid[::-1] == valid

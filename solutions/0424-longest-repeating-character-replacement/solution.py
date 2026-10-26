class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # AAAA
        # l  r
        # k = 2 -> 1 -> 0

        # AABABBA
        # l r   
        # k = 0


        # AABBAAAABBB
        # l        r
        # 2
        res = 1
        charset = set(s)

        n = len(s)
        for c in charset:
            l = 0
            count = 0

            for r in range(n):
                if s[r] != c:
                    count += 1
                    while count > k:
                        if s[l] != c:
                            count -= 1
                        l += 1
                
                res = max(res, r - l + 1)

        return res

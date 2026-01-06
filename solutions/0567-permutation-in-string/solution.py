class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        hm1 = {}
        hm2 = {}

        for i in range(n):
            hm1[s1[i]] = hm1.get(s1[i], 0) + 1
            hm2[s2[i]] = hm2.get(s2[i], 0) + 1
        
        if hm1 == hm2:
            return True
        
        for i in range(0, m - n):
            hm2[s2[i]] -= 1
            if hm2[s2[i]] <= 0:
                del hm2[s2[i]]

            hm2[s2[i+n]] = hm2.get(s2[i+n], 0) + 1

            if hm1 == hm2:
                return True
        
        return False

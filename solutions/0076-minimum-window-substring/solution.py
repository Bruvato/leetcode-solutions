class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        countT = {}
        window = {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have = 0
        need = len(countT)

        minLen = n
        res = ""

        l = 0

        for r in range(n):
            cr = s[r]
            window[cr] = window.get(cr, 0) + 1

            if cr in countT and window[cr] == countT[cr]:
                have += 1
            
            while have == need:
                if r - l + 1 <= minLen:
                    minLen = r - l + 1
                    res = s[l: r + 1]
                
                cl = s[l]
                window[cl] -= 1

                if cl in countT and window[cl] < countT[cl]:
                    have -= 1
                
                l += 1

        return res




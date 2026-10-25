class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hm = defaultdict(list)

        for s in strs:
            ht = [0] * 26
            
            for c in s:
                ht[ord(c) - ord('a')] += 1
            
            hm[tuple(ht)].append(s)
        
        return list(hm.values())

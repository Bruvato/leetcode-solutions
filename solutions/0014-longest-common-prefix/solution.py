class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)

        for i in range(len(strs[0])):

            for j in range(1, n):
                
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
                            
        return strs[0]

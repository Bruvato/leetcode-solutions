class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in s:
            if num - 1 not in s:
                count = 1
                while count + num in s:
                    count += 1
                if count > res:
                    res = count
        
        return res
                


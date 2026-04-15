class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return 1

        seen = set(nums)
        res = 0

        for num in seen:
            if num - 1 in seen:
                continue
            count = 1
            while count + num in seen:
                count += 1

            res = max(res, count)  

        return res


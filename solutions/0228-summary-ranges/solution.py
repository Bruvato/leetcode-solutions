class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ranges = []
        lower = nums[0]
        upper = nums[0]
        for num in nums[1:]:
            if num == 1 + upper:
                upper = num
            else:
                if lower == upper:
                    ranges.append(str(lower))
                else:
                    ranges.append(f"{lower}->{upper}")
                lower = num
                upper = num
                
        if lower == upper:
            ranges.append(str(lower))
        else:
            ranges.append(f"{lower}->{upper}")
        
        return ranges
        

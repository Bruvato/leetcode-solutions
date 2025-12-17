class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        n = len(nums)

        for i in range(n):
            num = nums[i]

            if target - num in seen:
                return [i, seen.get(target-num)]
            
            seen[num] = i

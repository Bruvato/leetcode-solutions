class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairing = {}

        for i, num in enumerate(nums):
            if target - num in pairing:
                return [i, pairing[target-num]]
            pairing[num] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, num in enumerate(nums):
            for i2, num2 in enumerate(nums):
                if i != i2 and num + num2 == target:
                    return [i, i2]


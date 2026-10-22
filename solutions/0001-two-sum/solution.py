class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}
        n = len(nums)

        for i in range(n):
            num = nums[i]

            if num in hm:
                return [i, hm[num]]
            else:
                hm[target - num] = i
        
        

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}

        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        val = 1
        key = nums[0]

        for k, v in hm.items():
            if v > val:
                val = v
                key = k


        return key

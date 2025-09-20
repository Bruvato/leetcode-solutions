class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = {}
        buckets = [[] for i in nums]
        res = []
        
        for num in nums:
            if num not in freqs:
                freqs[num] = 1
            else:
                freqs[num] = freqs[num] + 1

        for num, freq in freqs.items():
            buckets[len(nums) - freq - 1].append(num)

        for bucket in buckets:
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res

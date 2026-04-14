class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        if n == 1:
            return [nums[0]]

        
        hm = {}
        res = []
        heap = []

        for i in range(n):
            num = nums[i]

            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        
        for key, val in hm.items():
            heapq.heappush(heap, (-val, key))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res

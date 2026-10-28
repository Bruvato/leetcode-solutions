class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hm = {}


        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        
        heap = []

        for num, freq in hm.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        
        return res

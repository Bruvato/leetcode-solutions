class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = defaultdict(int)
        heap = []
        res = []

        for num in nums:
            hm[num] += 1

        for num, freq in hm.items():
            heapq.heappush(heap, (-freq, num))
        
        for i in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)


        return res

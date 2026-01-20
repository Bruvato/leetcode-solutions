class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        if len(stones) == 1:
            return stones[0]

        for s in stones:
            heapq.heappush(max_heap, -s)
        
        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)

            if x == y:
                continue
            else:
                heapq.heappush(max_heap, -abs(x - y))

        if len(max_heap) == 0:
            return 0
        
        return -heapq.heappop(max_heap)

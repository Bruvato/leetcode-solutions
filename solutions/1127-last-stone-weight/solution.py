class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)

        if n == 1:
            return stones[0]

        
        h = []

        for s in stones:
            heapq.heappush(h, -s)
        

        while len(h) >= 2:
            y = heapq.heappop(h)
            x = heapq.heappop(h)

            if x == y:
                continue
            
            heapq.heappush(h, y - x)
        
        if len(h) == 0:
            return 0
        
        return -heapq.heappop(h)

            


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)

        res = []
        heap = []

        for i in range(n):
            point = points[i]
            x, y = point
            dist = x * x + y * y

            heapq.heappush(heap, (-dist, point))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            dist, point = heapq.heappop(heap)
            res.append(point)


        return res

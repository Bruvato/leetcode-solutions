class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        heap = []
        q = deque()
        time = 0

        for t in tasks:
            hm[t] = hm.get(t, 0) + 1
        
        for task, freq in hm.items():
            heap.append((-freq, task))
        
        heapq.heapify(heap)

        while heap or q:
            time += 1

            if not heap:
                time = q[0][0]
            else:
                freq, task = heapq.heappop(heap)
                freq += 1
                if freq != 0:
                    q.append((time + n, freq, task))
            
            if q and q[0][0] <= time:
                t, freq, task = q.popleft()
                heapq.heappush(heap, (freq, task))
        
        return time


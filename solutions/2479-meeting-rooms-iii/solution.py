class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:

        meetings = sorted(meetings)

        busy = []
        free = []
        count = [0] * n

        for i in range(n):
            heapq.heappush(free, i)

        for start, end in meetings:

            while busy and busy[0][0] <= start:
                _, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                end_t, room = heapq.heappop(busy)

                if start >= end_t:
                    heapq.heappush(busy, (end, room))
                else:
                    offset = end_t - start
                    heapq.heappush(busy, (end + offset, room,))
            
            count[room] += 1
            
        return count.index(max(count))

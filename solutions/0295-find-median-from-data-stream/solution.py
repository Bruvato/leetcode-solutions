class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.h1, -num)

        if self.h1 and self.h2 and -self.h1[0] > self.h2[0]:
            heapq.heappush(self.h2, -heapq.heappop(self.h1))
        if len(self.h1) - len(self.h2) > 1:
            heapq.heappush(self.h2, -heapq.heappop(self.h1))
        if len(self.h2) - len(self.h1) > 1:
            heapq.heappush(self.h1, -heapq.heappop(self.h2))
        
        # print(self.h1)
        # print(self.h2)
            

    def findMedian(self) -> float:

        if len(self.h1) == len(self.h2):
            return (-self.h1[0] + self.h2[0]) / 2
        elif len(self.h1) > len(self.h2):
            return -self.h1[0]
        else:
            return self.h2[0]

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
'''
k = n / 2
4 -> 4
2 4 -> 
1 2 4 -> 2
1 2 3 4 ->
1 2 3 3 4
1 2 3 3 4 6 ->
1 2 3 3 4 5 6


[-1]
-2 -1
-3 [-2 -1]
-4 -3 -2 -1
-1 -2 -3 -4 -5

5 1 2 0

h1: 1 0
h2: 2 5 6 8
'''

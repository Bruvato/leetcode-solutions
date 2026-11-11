class HitCounter:

    def __init__(self):
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        i = timestamp % 300
        if self.times[i] == timestamp:
            self.hits[i] += 1
        else:
            self.times[i] = timestamp
            self.hits[i] = 1
        
    def getHits(self, timestamp: int) -> int:
        count = 0
        for i in range(300):
            if self.times[i] > timestamp - 300:
                count += self.hits[i]
        
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)

# 1 2 3 4 300 300 301
# x x x 

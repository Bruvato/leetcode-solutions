class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.hm[key]
        res = ""
        l = 0
        r = len(vals) - 1

        while l <= r:
            mid = (l + r) // 2
            if timestamp > vals[mid][1]:
                res = vals[mid][0]
                l = mid + 1
            elif timestamp < vals[mid][1]:
                r = mid - 1
            else:
                res = vals[mid][0]
                break
        
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

'''

foo -> (bar, 1) (bar2, 4)



1 2 3 4
  m
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        s, e = intervals[0]


        for start, end in intervals:
            if start <= e:
                e = max(e, end)
            else:
                res.append([s, e])
                s = start
                e = end
        
        res.append([s, e])
        return res
            

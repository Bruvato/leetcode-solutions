class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # --------------------
        #     -----
        #             ------
        # start [0, 5, 15]
        # end   [10, 20, 30]

        # -------
        # s [0]
        # e [5]

        # ------
        #.         ---
        # s [0, 6]
        # e [5, 10]

        # -----
        #.  ----------
        # [0, 3]
        # [5, 10]

        # -----
        #      -----
        # [0, 5]
        # [5, 10]

        n = len(intervals)
        count = 0
        res = 0
        starts = []
        ends = []
        s = 0
        e = 0

        for i in intervals:
            starts.append(i[0])
            ends.append(i[1])
        
        starts.sort()
        ends.sort()

        while s < n:
            if starts[s] < ends[e]:
                s += 1
                count += 1
                res = max(res, count)
            else:
                e += 1
                count -= 1
            
        
        return res


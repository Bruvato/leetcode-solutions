class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        '''
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

---  ----
 ----

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

---
 ----


    ---
   ---

--- --- ---
 --------

--- --- ---
 --------------

  --- --- ---
-----------

  --- --- ---
----------------

'''
        res = []

        ns, ne = newInterval
        for i in range(len(intervals)):
            start, end = intervals[i]

            if ne < start:
                res.append([ns, ne])
                return res + intervals[i:]
            elif end < ns:
                res.append(intervals[i])
            else:
                ns = min(ns, start)
                ne = max(ne, end)
        
        res.append([ns, ne])
        return res
        
        

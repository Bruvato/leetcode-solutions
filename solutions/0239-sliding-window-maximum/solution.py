class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        
        q = deque([])
        res = []
        n = len(nums)

        for r in range(n):
            while q and q[-1][0] < nums[r]:
                q.pop()

            q.append((nums[r], r)) # num -> idx
            while q[0][1] <= r - k:
                q.popleft()        
            
            if r + 1 >= k:
                res.append(q[0][0])
        return res
    
'''
Window position                Max
---------------               -----
3, -1
[1  3  -1] -3  5  3  6  7       3
3, -1, -3
 1 [3  -1  -3] 5  3  6  7       3
 5
 1  3 [-1  -3  5] 3  6  7       5
 5, 3
 1  3  -1 [-3  5  3] 6  7       5
 6
 1  3  -1  -3 [5  3  6] 7       6
 7
 1  3  -1  -3  5 [3  6  7]      7

'''

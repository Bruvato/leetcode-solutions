class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        h = []

        for num in nums:
            if num not in hm:
                hm[num] = 1
            else:
                hm[num] += 1
        
        for num, freq in hm.items():
            heapq.heappush(h, (freq, num))

            if len(h) > k:
                heapq.heappop(h)
        
        return [x[1] for x in h]


        '''
        1 2 3

        '''

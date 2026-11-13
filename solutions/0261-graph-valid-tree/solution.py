class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        hm = defaultdict(list)
        for e in edges:
            start, end = e

            hm[start].append(end)
            hm[end].append(start)
        
        q = deque([0])
        seen = {0}

        while q:
            node = q.popleft()

            for nei in hm[node]:
                if nei not in seen:
                    seen.add(nei)
                    q.append(nei)
        
        return len(seen) == n
            



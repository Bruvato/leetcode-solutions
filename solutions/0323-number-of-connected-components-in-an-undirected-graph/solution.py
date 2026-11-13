class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        hm = defaultdict(list)


        for edge in edges:
            s, e = edge

            hm[s].append(e)
            hm[e].append(s)
        
        seen = set()
        res = 0

        for i in range(n):
            if i in seen:
                continue
            
            res += 1
            seen.add(i)

            q = deque([i])

            while q:
                node = q.popleft()

                for nei in hm[node]:
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
        
        return res

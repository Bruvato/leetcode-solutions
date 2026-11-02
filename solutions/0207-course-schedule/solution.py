class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        g = defaultdict(list)
        # prereq -> course
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            if course == prereq:
                return False
            
            g[prereq].append(course)
            indegree[course] += 1
        
        taken = 0
        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                taken += 1
        
        while q:
            node = q.popleft()

            for nei in g[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    taken += 1
                    q.append(nei)
                
        return taken == numCourses




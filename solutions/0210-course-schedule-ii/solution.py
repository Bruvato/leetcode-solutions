class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        reqToCourse = {}
        indegree = [0] * numCourses

        for p in prerequisites:
            course, req = p

            if req not in reqToCourse:
                reqToCourse[req] = []
            
            reqToCourse[req].append(course)
            indegree[course] += 1

        roots = []

        for i in range(numCourses):
            if indegree[i] == 0:
                roots.append(i)
        
        q = deque(roots)
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nxt in reqToCourse.get(node, []):
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)
        
        if len(res) == numCourses:
            return res
        else:
            return []

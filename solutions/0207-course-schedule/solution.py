class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        g = defaultdict(list)
        # prereq -> course
        
        for course, prereq in prerequisites:
            if course == prereq:
                return False
            
            g[prereq].append(course)
        
        state = [0] * numCourses

        def dfs(node):
            if state[node] == 1:
                return False
            
            if state[node] == 2:
                return True
            
            state[node] = 1
            for nei in g[node]:
                if not dfs(nei):
                    return False
            
            state[node] = 2
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True




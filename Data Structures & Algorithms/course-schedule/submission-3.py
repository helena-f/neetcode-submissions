class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        if not prerequisites:
            return True
        for a, b in prerequisites:
            graph[b].append(a)

        # dfs cycle detection
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            if graph[course] == []:
                return True

            visited.add(course)
            for nei in graph[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            graph[course] = []
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return False
                


        # topological sort with bfs
        # q = deque([0])
        # visited = set()
        # while q:
        #     curr_course = q.popleft()
        #     visited.add(curr_course)
        #     for nei in graph[curr_course]:
        #         if nei in visited:
        #             return False
        #         q.append(nei)
        
        return True

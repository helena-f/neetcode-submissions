# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         if n == 1:
#             return 1
        
#         adj = defaultdict(list)
#         for start, end in edges:
#             adj[start].append(end)
#             adj[end].append(start)
#         # print(adj)
#         connected_num = 0
#         visited = set()
#         for edge in adj:
#             if edge not in visited:
#                 connected_num += 1
#                 cluster = []
#                 q = deque([edge])
#                 while q:
#                     curr_edge = q.popleft()
#                     if curr_edge in visited:
#                         continue
#                     cluster.append(curr_edge)
#                     visited.add(curr_edge)
#                     q.extend(adj[curr_edge])
#                 # print(cluster)

#         return connected_num
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if not visit[nei]:
                        visit[nei] = True
                        q.append(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res += 1
        return res
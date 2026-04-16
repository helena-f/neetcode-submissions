class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 1
        
        adj = defaultdict(list)
        for start, end in edges:
            adj[start].append(end)
            adj[end].append(start)
        # print(adj)
        connected_num = 0
        visited = set()
        for edge in range(n):
            if edge not in visited:
                connected_num += 1
                cluster = []
                q = deque([edge])
                while q:
                    curr_edge = q.popleft()
                    if curr_edge in visited:
                        continue
                    cluster.append(curr_edge)
                    visited.add(curr_edge)
                    q.extend(adj[curr_edge])
                # print(cluster)

        return connected_num

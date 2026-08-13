class Solution:
    def maxDistance(self, V, src, edges):
        adj = [[] for _ in range(V)]

        for u, v, w in edges:
            adj[u].append((v, w))

        # Topological Sort
        visited = [False] * V
        stack = []

        def dfs(node):
            visited[node] = True

            for v, w in adj[node]:
                if not visited[v]:
                    dfs(v)

            stack.append(node)

        for i in range(V):
            if not visited[i]:
                dfs(i)

        # Initialize distances
        dist = [-2**31] * V
        dist[src] = 0

        # Process in topological order
        while stack:
            u = stack.pop()

            if dist[u] == -2**31:
                continue

            for v, w in adj[u]:
                dist[v] = max(dist[v], dist[u] + w)

        return dist

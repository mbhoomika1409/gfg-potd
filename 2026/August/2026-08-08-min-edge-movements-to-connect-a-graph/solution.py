class Solution:
    def minEdgesReq(self, n, adj):
        parent = list(range(n))
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return False

            if size[a] < size[b]:
                a, b = b, a

            parent[b] = a
            size[a] += size[b]

            return True

        extra_edges = 0

        for u, v in adj:
            if not union(u, v):
                extra_edges += 1

        components = 0

        for i in range(n):
            if find(i) == i:
                components += 1

        needed = components - 1

        if extra_edges >= needed:
            return needed

        return -1

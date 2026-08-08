# Min Edge Movements to Connect a Graph

## Problem

Given a graph with `n` vertices numbered from `0` to `n-1` and `m` edges, we can perform the following operation:

* Remove one edge from anywhere in the graph.
* Add that edge between any two vertices.

Find the minimum number of operations required to make the graph connected.

If it is not possible to connect the graph, return `-1`.

## Examples

### Example 1

**Input:**

```text
n = 4
edges = [[0, 1], [0, 2], [1, 2]]
```

**Output:**

```text
1
```

**Explanation:**

The edge `(1, 2)` is an extra edge because it forms a cycle.

We can remove `(1, 2)` and add it between `(1, 3)`.

Therefore, the graph becomes connected in `1` operation.

### Example 2

**Input:**

```text
n = 6
edges = [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
```

**Output:**

```text
2
```

**Explanation:**

There are three connected components:

```text
{0, 1, 2, 3}
{4}
{5}
```

We need `2` edges to connect these three components.

There are enough extra edges available, so the minimum number of operations is `2`.

---

## Approach

We use **Disjoint Set Union (DSU)**, also called **Union-Find**.

DSU helps us efficiently find and merge connected components.

### Step 1: Find Extra Edges

For every edge `(u, v)`:

* If `u` and `v` belong to different components, merge them.
* If `u` and `v` already belong to the same component, this edge is an **extra edge**.

An extra edge can be removed and reused to connect two different components.

### Step 2: Count Connected Components

After processing all edges, count the number of connected components.

If there are `k` components, we need:

```text
k - 1
```

edges to connect all of them.

### Step 3: Check Extra Edges

If the number of extra edges is at least the number of edges required:

```text
extra_edges >= components - 1
```

then the graph can be connected.

Otherwise, it is impossible.

---

## Algorithm

1. Initialize `parent` and `size` arrays for DSU.
2. Process every edge.
3. Use `find()` to determine the component of each vertex.
4. Use `union()` to merge different components.
5. If an edge connects vertices already in the same component, increment `extra_edges`.
6. Count the number of connected components.
7. Calculate:

```text
needed = components - 1
```

8. If `extra_edges >= needed`, return `needed`.
9. Otherwise, return `-1`.

---

## Why Does This Work?

Suppose the graph has `k` disconnected components.

To connect them all, we must make exactly:

```text
k - 1
```

connections.

The only edges we can use for these new connections are **extra edges** that are already unnecessary inside existing components.

Therefore:

```text
If extra_edges >= k - 1:
    Answer = k - 1
Else:
    Answer = -1
```

---

## Python Solution

```python
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
```

---

## Complexity Analysis

### Time Complexity

```text
O(n + m)
```

DSU operations are nearly constant time due to **path compression** and **union by size**.

### Space Complexity

```text
O(n)
```

We use `parent` and `size` arrays of size `n`.

---

## Key Concept

> To connect `k` disconnected components, we need `k - 1` edges. Extra edges formed by cycles can be moved to connect these components.

## Topic

* Graph
* Disjoint Set Union (DSU)
* Union-Find
* Connected Components
* Cycle Detection

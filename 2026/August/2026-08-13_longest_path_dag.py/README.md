
# Longest Path in a Directed Acyclic Graph

## Date

13 August 2026

## Problem

Given a weighted Directed Acyclic Graph (DAG) with V vertices numbered from 0 to V - 1, and a source vertex src, find the longest distance from the source vertex to every other vertex.

Each edge is represented as:

[u, v, w]

where:

- u = starting vertex
- v = destination vertex
- w = weight of the edge

If a vertex cannot be reached from the source, its distance should be INT_MIN.

The driver code displays INT_MIN as INF.

---

## Example

### Input

V = 4
src = 0

edges = [
    [0, 1, 1],
    [0, 2, 1],
    [1, 2, 5],
    [3, 1, 2],
    [3, 2, -1]
]

### Output

[0, 1, 6, INF]

### Explanation

The source vertex is 0.

Vertex 0:

The distance from the source to itself is 0.

dist[0] = 0

Vertex 1:

There is an edge:

0 → 1

with weight 1.

Therefore:

dist[1] = 1

Vertex 2:

There are two possible paths from 0 to 2.

First path:

0 → 2

Distance:

1

Second path:

0 → 1 → 2

Distance:

1 + 5 = 6

We need the longest distance, so:

dist[2] = 6

Vertex 3:

There is no path from 0 to 3.

Therefore:

dist[3] = INT_MIN

The driver displays INT_MIN as:

INF

Final output:

[0, 1, 6, INF]

---

## Approach

Since the graph is a DAG (Directed Acyclic Graph), we can find the longest path using:

1. Adjacency List
2. Topological Sort
3. Dynamic Programming

---

## Step 1: Create an Adjacency List

The given edges are converted into an adjacency list.

For example:

0 → 1 (weight 1)
0 → 2 (weight 1)
1 → 2 (weight 5)
3 → 1 (weight 2)
3 → 2 (weight -1)

The adjacency list stores the destination vertex and its edge weight.

Code:

adj = [[] for _ in range(V)]

for u, v, w in edges:
    adj[u].append((v, w))

For the given example:

0 → [(1, 1), (2, 1)]
1 → [(2, 5)]
2 → []
3 → [(1, 2), (2, -1)]

---

## Step 2: Perform Topological Sort

A topological ordering arranges the vertices so that for every directed edge:

u → v

u appears before v.

Because the graph is a DAG, a topological ordering always exists.

DFS is used to perform the topological sort.

Code:

visited = [False] * V
stack = []

def dfs(node):
    visited[node] = True

    for v, w in adj[node]:
        if not visited[v]:
            dfs(v)

    stack.append(node)

The vertex is added to the stack only after all its neighbouring vertices have been processed.

stack.append(node)

This helps us obtain the vertices in topological order when they are popped from the stack.

---

## Step 3: Initialize the Distance Array

We need to store the longest distance from the source to every vertex.

Initially, every vertex is unreachable.

Therefore, all distances are initialized to INT_MIN.

Code:

dist = [-2**31] * V

Then the source vertex is assigned distance 0.

Code:

dist[src] = 0

For example:

src = 0

Initially:

dist = [0, INT_MIN, INT_MIN, INT_MIN]

This means:

- Vertex 0 has distance 0
- Vertex 1 is currently unreachable
- Vertex 2 is currently unreachable
- Vertex 3 is currently unreachable

---

## Step 4: Process Vertices in Topological Order

After topological sorting, we process each vertex in topological order.

Code:

while stack:
    u = stack.pop()

If the current vertex cannot be reached from the source, we skip it.

Code:

if dist[u] == -2**31:
    continue

This prevents us from calculating paths from unreachable vertices.

---

## Step 5: Update the Longest Distance

For every edge:

u → v

with weight w, we calculate:

dist[u] + w

and compare it with the current distance of v.

We keep the maximum value.

Code:

dist[v] = max(dist[v], dist[u] + w)

For example:

dist[0] = 0

For the edge:

0 → 1
weight = 1

We calculate:

dist[1] = max(INT_MIN, 0 + 1)
        = 1

So:

dist[1] = 1

Then for:

1 → 2
weight = 5

We calculate:

dist[2] = max(INT_MIN, 1 + 5)
        = 6

Therefore:

dist[2] = 6

---

## Complete Algorithm

1. Create an adjacency list from the given edges.

2. Perform DFS-based topological sorting.

3. Initialize all distances to INT_MIN.

4. Set dist[src] = 0.

5. Process vertices in topological order.

6. For every edge u → v with weight w:

   dist[v] = max(dist[v], dist[u] + w)

7. Return the distance array.

---

## Why Does This Work?

The important property is that the graph is a DAG.

Since there are no cycles, we can process the vertices in topological order.

When a vertex u is processed, the vertices that can come before u have already been processed.

Therefore, we can safely calculate the longest distance to the next vertex.

For every edge:

u → v

we perform:

dist[v] = max(dist[v], dist[u] + w)

This ensures that the largest possible distance is stored for every reachable vertex.

---

## Important Line

The most important line of the solution is:

dist[v] = max(dist[v], dist[u] + w)

It means:

"If going from the source to v through u produces a longer path, update the distance of v."

For example, suppose:

dist[u] = 4
w = 6
dist[v] = 7

Then:

dist[u] + w = 4 + 6 = 10

Since 10 > 7:

dist[v] = 10

---

## Why Use INT_MIN?

The problem requires INT_MIN for unreachable vertices.

In Python, we use:

-2**31

which is equal to:

-2147483648

Therefore:

dist = [-2**31] * V

means that initially every vertex is considered unreachable.

After processing the graph, vertices that are still -2**31 are unreachable from the source.

---

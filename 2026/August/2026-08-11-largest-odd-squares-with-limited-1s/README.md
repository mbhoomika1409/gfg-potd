# Largest Odd Squares with Limited 1s

## Problem

Given a binary matrix `mat[][]` of size `n × m` and an integer `k`, process a list of queries.

Each query contains coordinates `[i, j]`, representing the center of a square.

For every query, find the largest odd-sized square centered at `(i, j)` such that the square contains at most `k` ones.

If no valid odd-sized square exists, return `-1`.

---

## Example

### Input

```text
mat = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0]
]

queries = [[1, 2]]
k = 9
```

### Output

```text
[3]
```

### Explanation

For query `(1, 2)`, the largest valid square is:

```text
3 × 3
```

It spans rows `0 to 2` and columns `1 to 3`.

The square contains `6` ones, which is less than or equal to `k = 9`.

Therefore, the answer is `3`.

---

## Approach

We use two techniques:

1. **2D Prefix Sum**
2. **Binary Search**

### 1. 2D Prefix Sum

We create a prefix sum matrix where:

```text
prefix[i][j]
```

stores the number of ones in the rectangle from the top-left corner to `(i-1, j-1)`.

This allows us to find the number of ones inside any square in `O(1)` time.

The number of ones in rectangle `(r1, c1)` to `(r2, c2)` is:

```text
prefix[r2 + 1][c2 + 1]
- prefix[r1][c2 + 1]
- prefix[r2 + 1][c1]
+ prefix[r1][c1]
```

---

### 2. Represent the Square Using Radius

For a center `(i, j)`:

```text
radius = 0 → 1 × 1
radius = 1 → 3 × 3
radius = 2 → 5 × 5
radius = 3 → 7 × 7
```

The side length is:

```text
2 × radius + 1
```

For a given radius `r`:

```text
top    = i - r
bottom = i + r
left   = j - r
right  = j + r
```

---

### 3. Binary Search

For each query, we find the maximum possible radius that stays inside the matrix.

If a square contains at most `k` ones:

```text
ones <= k
```

then the square is valid, so we try a larger radius.

Otherwise, we try a smaller radius.

Finally:

```text
answer = 2 × best_radius + 1
```

---

## Algorithm

1. Build the 2D prefix sum matrix.
2. For each query `(i, j)`:

   * Find the maximum possible radius.
   * Check whether the `1 × 1` square is valid.
   * Apply binary search on the radius.
   * Count the number of ones using the prefix sum.
   * Store the largest valid odd side length.
3. Return the answers.

---

## Complexity

Let:

* `n` = number of rows
* `m` = number of columns
* `q` = number of queries

### Time Complexity

Building prefix sum:

```text
O(n × m)
```

Each query uses binary search:

```text
O(log(min(n, m)))
```

Total:

```text
O(n × m + q × log(min(n, m)))
```

### Space Complexity

```text
O(n × m)
```

for the 2D prefix sum matrix.

---

## Key Concepts

* 2D Prefix Sum
* Binary Search
* Matrix
* Dynamic Programming
* Searching
* Range Sum Query

---

## GFG POTD

**Problem:** Largest Odd Squares with Limited 1s
**Difficulty:** Medium
**Platform:** GeeksforGeeks
**Date:** 2026-08-11

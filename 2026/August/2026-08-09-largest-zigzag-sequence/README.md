# Largest Zigzag Sequence

## Problem

Given a square matrix `mat[][]` of size `n × n`, a zigzag sequence starts from the top row and ends at the bottom row.

Two consecutive elements of the sequence cannot belong to the same column.

Return the maximum sum of such a zigzag sequence.

---

## Examples

### Example 1

**Input:**

```text
mat[][] = [[3, 1, 2],
           [4, 8, 5],
           [6, 9, 7]]
```

**Output:**

```text
18
```

**Explanation:**

One optimal zigzag sequence is:

```text
3 → 8 → 7
```

The selected columns are:

```text
0 → 1 → 2
```

No two consecutive elements belong to the same column.

The sum is:

```text
3 + 8 + 7 = 18
```

---

### Example 2

**Input:**

```text
mat[][] = [[1, 2, 4],
           [3, 9, 6],
           [11, 3, 15]]
```

**Output:**

```text
28
```

**Explanation:**

One optimal zigzag sequence is:

```text
4 → 9 → 15
```

The selected columns are:

```text
2 → 1 → 2
```

Consecutive elements are from different columns.

The sum is:

```text
4 + 9 + 15 = 28
```

---

## Approach

This problem can be solved using **Dynamic Programming**.

We process the matrix row by row.

### DP Definition

Let:

```text
dp[j]
```

represent the maximum sum of a valid zigzag sequence ending at column `j` of the current row.

---

## Step 1: Initialize the First Row

For the first row, we can choose any element because there is no previous element.

Therefore:

```python
dp = mat[0][:]
```

For example:

```text
mat[0] = [3, 1, 2]

dp = [3, 1, 2]
```

---

## Step 2: Process the Remaining Rows

For every element `mat[i][j]`, we need to find the best possible sequence from the previous row.

But there is one important condition:

> The previous element cannot belong to the same column.

Therefore, for column `j`, we find the maximum value of:

```text
dp[k] where k != j
```

Then:

```text
new_dp[j] = mat[i][j] + best
```

---

## Step 3: Update DP

After calculating all columns for the current row:

```python
dp = new_dp
```

Now `dp` contains the best possible sums for the current row.

---

## Step 4: Find the Answer

After processing all rows, the answer is the maximum value in the final DP array.

```python
return max(dp)
```

---

## Dry Run

Consider the matrix:

```text
3  1  2
4  8  5
6  9  7
```

### Initial DP

From the first row:

```text
dp = [3, 1, 2]
```

---

### Processing Second Row

For column `0`, we cannot use `dp[0]`.

```text
best = max(1, 2) = 2
```

Therefore:

```text
4 + 2 = 6
```

For column `1`, we cannot use `dp[1]`.

```text
best = max(3, 2) = 3
```

Therefore:

```text
8 + 3 = 11
```

For column `2`, we cannot use `dp[2]`.

```text
best = max(3, 1) = 3
```

Therefore:

```text
5 + 3 = 8
```

Now:

```text
dp = [6, 11, 8]
```

---

### Processing Third Row

For column `0`:

```text
6 + max(11, 8) = 17
```

For column `1`:

```text
9 + max(6, 8) = 17
```

For column `2`:

```text
7 + max(6, 11) = 18
```

Now:

```text
dp = [17, 17, 18]
```

Therefore:

```text
answer = max(dp)
       = 18
```

The optimal sequence is:

```text
3 → 8 → 7
```

---

## Algorithm

1. Initialize `dp` with the first row of the matrix.
2. Traverse the matrix from the second row.
3. For every column `j`:

   * Check every column `k` from the previous row.
   * Ignore `k == j` because consecutive elements cannot use the same column.
   * Find the maximum valid previous DP value.
   * Add the current matrix value to it.
4. Store the result in `new_dp`.
5. Replace `dp` with `new_dp`.
6. After processing all rows, return `max(dp)`.

---

## Complexity Analysis

### Time Complexity

For every cell, we check all columns of the previous row.

There are `n × n` cells and each cell checks `n` columns.

Therefore:

```text
O(n³)
```

### Space Complexity

We use two arrays of size `n`:

```text
dp
new_dp
```

Therefore:

```text
O(n)
```

---

## Constraints

```text
1 ≤ n ≤ 100
1 ≤ mat[i][j] ≤ 1000
```

---

## Key Idea

The important condition in this problem is:

> Two consecutive elements cannot belong to the same column.

For every element in the current row, we therefore choose the maximum DP value from the previous row whose column is different from the current column.

---

## Solution Code

```python
class Solution:
    def zigzagSequence(self, mat):
        n = len(mat)

        dp = mat[0][:]

        for i in range(1, n):
            new_dp = [0] * n

            for j in range(n):
                best = 0

                for k in range(n):
                    if k != j:
                        best = max(best, dp[k])

                new_dp[j] = mat[i][j] + best

            dp = new_dp

        return max(dp)
```

---

## Input

```text
3 3 1 2 4 8 5 6 9 7
```

Matrix:

```text
3  1  2
4  8  5
6  9  7
```

## Output

```text
18
```

## Optimal Zigzag Sequence

```text
3 → 8 → 7
```

## Sum

```text
3 + 8 + 7 = 18
```

---

## Platform

**GeeksforGeeks**

## Problem Type

**Problem of the Day (POTD)**

## Difficulty

**Easy**

## Topic

**Dynamic Programming**

## Language

**Python 3**

---

## Tags

* Dynamic Programming
* Matrix
* Optimization
* GFG POTD
* Python
* DP
* Matrix DP

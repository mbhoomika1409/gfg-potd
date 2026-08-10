# High Effort vs Low Effort

## Problem

Given two integer arrays `h[]` and `l[]`, where:

* `h[i]` represents the number of tasks that can be completed on day `i` by performing a **high-effort task**.
* `l[i]` represents the number of tasks that can be completed on day `i` by performing a **low-effort task**.

For each day, we can choose exactly one of the following:

1. Perform no task.
2. Perform a low-effort task.
3. Perform a high-effort task.

A high-effort task can only be performed on the first day or if **no task was performed on the previous day**.

Find the maximum total number of tasks that can be completed.

---

## Example 1

### Input

```text
h[] = [2, 8, 1]
l[] = [1, 2, 1]
```

### Output

```text
9
```

### Explanation

Choose:

* Day 0 → Low-effort task = `1`
* Day 1 → High-effort task = `8`
* Day 2 → No task = `0`

Total:

```text
1 + 8 + 0 = 9
```

Therefore, the maximum number of tasks is `9`.

---

## Example 2

### Input

```text
h[] = [3, 6, 8, 7, 6]
l[] = [1, 5, 4, 5, 3]
```

### Output

```text
20
```

### Explanation

Choose:

* Day 0 → High-effort task = `3`
* Day 1 → Low-effort task = `5`
* Day 2 → Low-effort task = `4`
* Day 3 → Low-effort task = `5`
* Day 4 → Low-effort task = `3`

Total:

```text
3 + 5 + 4 + 5 + 3 = 20
```

Therefore, the maximum number of tasks is `20`.

---

## Approach

This problem can be solved using **Dynamic Programming**.

For each day, there are three possible choices:

### 1. Low-effort task

We can perform a low-effort task even if a task was performed on the previous day.

So:

```text
low = prev1 + l[i]
```

where `prev1` is the maximum number of tasks obtained up to the previous day.

### 2. High-effort task

A high-effort task can only be performed if **no task was performed on the previous day**.

Therefore, when choosing a high-effort task on day `i`, we use the result from two days before:

```text
high = prev2 + h[i]
```

where `prev2` represents the maximum result up to the day before the previous day.

### 3. No task

We can also choose to perform no task today.

Therefore:

```text
nothing = prev1
```

### Choose the Maximum

For every day:

```text
current = max(low, high, nothing)
```

Then update the previous states:

```text
prev2 = prev1
prev1 = current
```

This keeps only two previous DP values instead of using a complete DP array.

---

## Algorithm

1. Initialize `prev1` with the maximum of the high-effort and low-effort task on the first day.
2. Initialize `prev2 = 0`.
3. Traverse the array from the second day.
4. Calculate the three possible options:

   * Low-effort task.
   * High-effort task.
   * No task.
5. Take the maximum of the three options.
6. Update `prev2` and `prev1`.
7. Return `prev1`.

---

## Complexity

### Time Complexity

```text
O(n)
```

We visit each day exactly once.

### Auxiliary Space

```text
O(1)
```

Only two variables are used to store the previous DP states.

---

## Key Insight

The important condition is:

> A high-effort task cannot be performed if a task was performed on the previous day.

Therefore, when choosing a high-effort task on day `i`, we use the result from two days before.

```text
High effort → prev2 + h[i]
Low effort  → prev1 + l[i]
No task     → prev1
```

We choose the maximum among these three possibilities.

This gives an efficient solution with:

```text
Time Complexity  → O(n)
Space Complexity → O(1)
```

---

## Topic

* Dynamic Programming
* Space Optimization
* Arrays

---

## Solution

The corresponding Python solution is available in `solution.py`.

The GFG function name is:

```python
maxTask
```

because the GFG driver code calls:

```python
ob.maxTask(high, low)
```

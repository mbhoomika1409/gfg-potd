# Friends Pairing Problem

**Difficulty:** Medium

## Problem Statement

Given `n` friends, each friend can either:

- Stay single.
- Pair up with exactly one other friend.

Each friend can be paired only once.

Find the total number of possible ways in which all friends can remain single or be paired.

---

## Examples

### Example 1

Input:

```text
n = 3
```

Output:

```text
4
```

Explanation:

```
{1}, {2}, {3}
{1}, {2,3}
{1,2}, {3}
{1,3}, {2}
```

---

### Example 2

Input:

```text
n = 2
```

Output:

```text
2
```

---

### Example 3

Input:

```text
n = 1
```

Output:

```text
1
```

---

## Intuition

For every friend, we have only **two choices**:

### Choice 1: Stay Single

- One friend remains single.
- Solve the remaining `n-1` friends.

Ways:

```
f(n-1)
```

---

### Choice 2: Form a Pair

- Select one friend.
- They can pair with any of the remaining `(n-1)` friends.
- After forming the pair, solve the remaining `n-2` friends.

Ways:

```
(n-1) × f(n-2)
```

---

## Recurrence Relation

```
f(n) = f(n-1) + (n-1) × f(n-2)
```

Base Cases:

```
f(1) = 1
f(2) = 2
```

---

## Why This Formula Works

Suppose there are **5 friends**.

Take Friend 1.

### Case 1

Friend 1 stays single.

Remaining friends:

```
2 3 4 5
```

Ways:

```
f(4)
```

---

### Case 2

Friend 1 forms a pair.

Possible partners:

```
(1,2)
(1,3)
(1,4)
(1,5)
```

There are

```
4 choices
```

After pairing,

Remaining friends:

```
3 friends
```

Ways:

```
4 × f(3)
```

So,

```
f(5)=f(4)+4×f(3)
```

---

## Approach

Since `n ≤ 18`, recursion works, but iterative Dynamic Programming is more efficient.

Store only the last two computed values instead of an entire DP array.

Steps:

1. Handle base cases.
2. Start from 3 up to n.
3. Apply the recurrence.
4. Update previous answers.
5. Return the final result.

---

## Algorithm

1. If `n == 1`, return 1.
2. If `n == 2`, return 2.
3. Initialize

```
prev2 = 1
prev1 = 2
```

4. For every `i` from `3` to `n`

```
current = prev1 + (i-1) × prev2
```

5. Shift values

```
prev2 = prev1
prev1 = current
```

6. Return `prev1`.

---

## Dry Run

### n = 5

Initially

```
prev2 = 1
prev1 = 2
```

i = 3

```
current = 2 + 2×1
        = 4
```

Update

```
prev2 = 2
prev1 = 4
```

---

i = 4

```
current = 4 + 3×2
        = 10
```

Update

```
prev2 = 4
prev1 = 10
```

---

i = 5

```
current = 10 + 4×4
        = 26
```

Answer

```
26
```

---

## Complexity Analysis

### Time Complexity

```
O(n)
```

Only one traversal from `3` to `n`.

### Auxiliary Space

```
O(1)
```

Only three variables are used.

---

## Python Solution

```python
class Solution:
    def countFriendsPairings(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        prev2 = 1
        prev1 = 2

        for i in range(3, n + 1):
            current = prev1 + (i - 1) * prev2
            prev2 = prev1
            prev1 = current

        return prev1
```

---

## Key Learning

- Dynamic Programming with recurrence relations.
- Converting recursion into an iterative solution.
- Space optimization using only previous states.
- Identifying choices (single or pair) to derive the recurrence.

---

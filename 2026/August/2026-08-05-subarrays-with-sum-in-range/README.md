# Subarrays with Sum in Range

## Problem

Given an integer array `arr[]` and two integers `l` and `r`, count the number of contiguous subarrays whose sum lies in the range **[l, r]** (inclusive).

---

## Example

### Input

```text
arr = [1, 2, 3]
l = 3
r = 5
```

### Output

```text
3
```

---

## Approaches

### 1. Brute Force

- Generate every possible subarray.
- Calculate the sum of each subarray.
- Count the subarrays whose sum lies in the range `[l, r]`.

**Time Complexity:** `O(n²)`

---

### 2. Optimal Approach (Sliding Window + Inclusion-Exclusion)

#### Intuition

Instead of counting subarrays whose sum lies in `[l, r]` directly, calculate:

```
Subarrays with sum ≤ r
-
Subarrays with sum ≤ (l - 1)
```

Since,

```
Subarrays with sum in [l, r]
=
Subarrays with sum ≤ r
-
Subarrays with sum ≤ (l - 1)
```

Create a helper function `count(k)` that counts subarrays whose sum is at most `k`.

---

## Algorithm

1. Create a helper function `count(k)`.
2. Use two pointers (`left` and `right`) to maintain a sliding window.
3. Expand the window by moving the right pointer.
4. If the current sum becomes greater than `k`, shrink the window from the left.
5. Add `right - left + 1` to the answer since all those subarrays are valid.
6. Return `count(r) - count(l - 1)`.

---

## Dry Run

### Input

```text
arr = [1,2,3]
l = 3
r = 5
```

### count(5)

| Right | Window | Sum | Added | Total |
|------:|--------|----:|------:|------:|
|0|[1]|1|1|1|
|1|[1,2]|3|2|3|
|2|[2,3]|5|2|5|

```
count(5) = 5
```

### count(2)

| Right | Window | Sum | Added | Total |
|------:|--------|----:|------:|------:|
|0|[1]|1|1|1|
|1|[2]|2|1|2|
|2|[]|0|0|2|

```
count(2) = 2
```

Final Answer

```
count(5) - count(2)
= 5 - 2
= 3
```

---

## Time Complexity

- `count(k)` → `O(n)`
- Called twice

**Overall Time Complexity:** `O(n)`

---

## Auxiliary Space

**O(1)**

---

## Key Takeaways

- Sliding Window works because the array contains non-negative elements.
- Instead of solving the range directly, compute two prefix counts.
- Every element enters and leaves the sliding window at most once.
- The solution runs in linear time.

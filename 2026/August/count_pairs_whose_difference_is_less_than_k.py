# Count Pairs Whose Difference is Less than K (POTD)

## Problem Statement

Given an array `arr[]` of positive integers and an integer `k`, find the total number of unique pairs whose **absolute difference** is **strictly less than `k`**.

> **Note:** Pair `(i, j)` is considered the same as `(j, i)`.

### Example

**Input**

```text
arr = [1, 10, 4, 2]
k = 3
```

**Output**

```text
2
```

**Explanation**

The valid pairs are:

- (1, 2)
- (4, 2)

Hence, the answer is **2**.

---

# Approach (Sorting + Two Pointers)

## Idea

The brute-force solution checks every possible pair, resulting in **O(n²)** time complexity, which is too slow for large inputs.

To optimize:

- Sort the array.
- Use two pointers (`i` and `j`).
- Move the second pointer forward while the difference remains less than `k`.
- Count all valid pairs for each position.

This avoids checking every pair individually and improves efficiency.

---

# Algorithm

1. Sort the array.
2. Initialize:
   - `count = 0`
   - `j = 0`
3. Traverse the array using pointer `i`.
4. Move pointer `j` forward while `arr[j] - arr[i] < k`.
5. Add `(j - i - 1)` to the answer.
6. Return the total count.

---

# Python Code

```python
class Solution:
    def countPairs(self, arr, k):
        arr.sort()
        n = len(arr)
        count = 0
        j = 0

        for i in range(n):
            while j < n and arr[j] - arr[i] < k:
                j += 1

            count += (j - i - 1)

        return count
```

---

# Complexity Analysis

- **Time Complexity:** `O(n log n)`
  - Sorting takes `O(n log n)`.
  - Two pointers traverse the array in `O(n)`.

- **Auxiliary Space:** `O(1)`

---

# Key Takeaways

- Uses **Sorting + Two Pointers**.
- Eliminates the need for nested loops.
- Much faster than the brute-force approach.
- Suitable for large input sizes and accepted by GeeksforGeeks.

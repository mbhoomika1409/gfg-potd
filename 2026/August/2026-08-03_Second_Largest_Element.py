# GFG POTD – Maximum Sum Subarray of Size at Least K

## Problem

Given an integer array `arr[]` and an integer `k`, find the maximum sum of any contiguous subarray having **at least `k` elements**.

## Approach

- Use **Kadane's Algorithm** to compute the maximum subarray sum ending at every index and store it in the `max_end` array.
- Calculate the sum of the first `k` elements using a **sliding window**.
- Initialize the answer with this window sum.
- Slide the window across the array:
  - Add the new element entering the window.
  - Remove the element leaving the window.
  - Update the answer with the current window sum.
  - Extend the current window by adding `max_end[i-k]` (the best subarray ending just before the window) if it increases the total sum.
- Return the maximum sum obtained.

## Time Complexity

- **O(n)**

## Space Complexity

- **O(n)** (for the `max_end` array)

## Concepts Used

- Kadane's Algorithm
- Sliding Window
- Dynamic Programming (DP)
- Arrays

## Python Solution

```python
class Solution:
    def maxSumWithK(self, arr, k):
        n = len(arr)

        max_end = [0] * n
        max_end[0] = arr[0]

        for i in range(1, n):
            max_end[i] = max(arr[i], max_end[i - 1] + arr[i])

        curr_sum = sum(arr[:k])
        ans = curr_sum

        for i in range(k, n):
            curr_sum += arr[i] - arr[i - k]
            ans = max(ans, curr_sum)
            ans = max(ans, curr_sum + max_end[i - k])

        return ans
```

## Example

**Input**

```text
arr = [1, 2, 3, -10, 4, 5]
k = 2
```

**Output**

```text
9
```

**Explanation**

The maximum sum subarray with at least `2` elements is `[4, 5]`, whose sum is `9`.

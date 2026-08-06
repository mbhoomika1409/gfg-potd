# Minimum Increment or Double Operations to Convert

**Difficulty:** Medium  
**Platform:** GeeksforGeeks (GFG POTD)

---

# Problem Statement

Given an array `arr[]`. Initially, there is another array of the same size containing only `0`s.

You can perform only two operations:

1. Increase any one element by `1`.
2. Double the values of **all** elements in the array simultaneously.

Return the **minimum number of operations** required to convert the all-zero array into the given target array.

---

# Example

### Example 1

**Input**

```text
arr = [16, 16, 16]
```

**Output**

```text
7
```

### Explanation

```
[0,0,0]

Increase each element once
↓

[1,1,1]        (3 operations)

Double four times

[2,2,2]
↓

[4,4,4]
↓

[8,8,8]
↓

[16,16,16]

Total = 3 + 4 = 7
```

---

### Example 2

**Input**

```text
arr = [2,3]
```

**Output**

```text
4
```

### Explanation

```
[0,0]

↓

[1,1]      (+1 twice)

↓

[2,2]      (double)

↓

[2,3]      (+1 once)

Total = 4 operations
```

---

# Intuition

At first glance, solving the problem from **0 → target** seems difficult because there are many possible sequences of operations.

Instead, think in reverse.

Rather than asking:

> How do I create this number?

Ask:

> If this number already exists, what was the previous step?

Working backwards makes every step deterministic.

---

# Key Observation

There are only two possible operations.

### Case 1 : Number is Odd

Example

```
13

↓

12
```

The last operation **cannot** be doubling because doubling always produces an even number.

Therefore, the last forward operation **must have been an increment**.

So,

- Count one increment.
- Subtract 1.

---

### Case 2 : Number is Even

Example

```
12

↓

6
```

An even number could only have come from doubling.

So,

- Count one doubling.
- Divide by 2.

Repeat until the number becomes zero.

---

# Why Count Every Increment?

Increment affects **only one element**.

For example,

```
[2,3]
```

The increments required for `2` cannot help create `3`.

Therefore, every odd number encountered while reversing contributes one increment.

So,

```
Total increments
=
Sum of increments required by every element
```

---

# Why Take Only Maximum Doubles?

Doubling affects **every element simultaneously**.

Example

```
[16,16,16]
```

Each element individually needs

```
4 doubles
```

But one doubling operation doubles **all elements together**.

```
[1,1,1]

↓

[2,2,2]

↓

[4,4,4]

↓

[8,8,8]

↓

[16,16,16]
```

So we don't add all doubling counts.

We only need

```
Maximum doubles required among all elements.
```

---

# Algorithm

1. Initialize

```
increments = 0
max_doubles = 0
```

2. Traverse every number.

3. While number > 0

- If odd
    - increment answer
    - subtract one

- Else
    - count one double
    - divide by two

4. Store the maximum doubles among all numbers.

5. Return

```
increments + max_doubles
```

---

# Dry Run

Input

```
arr = [2,3]
```

### Number = 2

```
2

↓

1

Double = 1

↓

0

Increment = 1
```

---

### Number = 3

```
3

↓

2

Increment = 2

↓

1

Double = 1

↓

0

Increment = 3
```

Maximum doubles

```
max(1,1)=1
```

Answer

```
3 + 1 = 4
```

---

# Time Complexity

Each number is repeatedly divided by 2.

For every element

```
O(log(arr[i]))
```

Overall

```
O(N × log(Max Element))
```

---

# Space Complexity

```
O(1)
```

---

# Key Learning

This problem teaches an important technique:

- When forward simulation has too many choices, think in reverse.
- Odd numbers indicate an increment operation.
- Even numbers indicate a doubling operation.
- Since doubling affects the entire array, count only the maximum doubling operations.
- Reverse simulation is a common interview and competitive programming pattern.

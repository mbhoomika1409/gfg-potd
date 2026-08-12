Adventure in a Maze

Difficulty: Hard
Topic: Dynamic Programming, Matrix
Platform: GeeksforGeeks (POTD)

Problem Statement

Given an n x n grid where each cell contains 1, 2, or 3:

1 → move Right only
2 → move Down only
3 → move Right or Down

Start at (0, 0), reach (n-1, n-1), following each cell's allowed direction(s).

Adventure of a path = sum of all cell values visited (including entry & exit).

Find:

Total number of distinct valid paths (mod 10^9 + 7)
Maximum possible Adventure among all valid paths

Return as [totalPaths, maxAdventure].

Examples

Example 1:

Input: grid = [[3, 2], [1, 3]]
Output: [2, 8]

Path 1: (0,0)->(0,1)->(1,1) => 3+2+3 = 8
Path 2: (0,0)->(1,0)->(1,1) => 3+1+3 = 7
Max Adventure = 8, Total Paths = 2

Example 2:

Input: grid = [[1,1,3,2,1],[3,2,2,1,2],[1,3,3,1,3],[1,2,3,1,2],[1,1,1,3,1]]
Output: [4, 18]
4 valid paths exist with sums 18, 17, 17, 16 → max = 18
Approach (DP on Grid)

Maintain two DP tables:

count[i][j] → number of distinct valid paths from (0,0) to (i,j)
maxSum[i][j] → maximum Adventure (sum) to reach (i,j)

Key rule (movement validity):

You can arrive at (i,j) from the left (i,j-1) only if grid[i][j-1] is 1 or 3 (that cell allows moving Right)
You can arrive at (i,j) from the top (i-1,j) only if grid[i-1][j] is 2 or 3 (that cell allows moving Down)

This is the trick of the problem — you check the previous cell's value, not the current cell's, to decide if the move into the current cell was legal.

Base case: count[0][0] = 1, maxSum[0][0] = grid[0][0]

Transition:

if left neighbor allows Right:
    count[i][j] += count[i][j-1]
    maxSum[i][j] = max(maxSum[i][j], maxSum[i][j-1] + grid[i][j])

if top neighbor allows Down:
    count[i][j] += count[i-1][j]
    maxSum[i][j] = max(maxSum[i][j], maxSum[i-1][j] + grid[i][j])

Answer: count[n-1][n-1] and maxSum[n-1][n-1]

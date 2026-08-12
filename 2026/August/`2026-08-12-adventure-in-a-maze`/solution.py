class Solution:
    def findWays(self, grid):
        MOD = 10**9 + 7
        n = len(grid)
        
        count = [[0] * n for _ in range(n)]
        maxSum = [[-1] * n for _ in range(n)]
        
        count[0][0] = 1
        maxSum[0][0] = grid[0][0]
        
        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                ways = 0
                best = -1
                
                # coming from left: (i, j-1) must allow Right (1 or 3)
                if j > 0 and grid[i][j-1] in (1, 3) and count[i][j-1] > 0:
                    ways += count[i][j-1]
                    best = max(best, maxSum[i][j-1])
                
                # coming from top: (i-1, j) must allow Down (2 or 3)
                if i > 0 and grid[i-1][j] in (2, 3) and count[i-1][j] > 0:
                    ways += count[i-1][j]
                    best = max(best, maxSum[i-1][j])
                
                count[i][j] = ways % MOD
                if best != -1:
                    maxSum[i][j] = best + grid[i][j]
        
        totalPaths = count[n-1][n-1]
        maxAdventure = maxSum[n-1][n-1] if maxSum[n-1][n-1] != -1 else 0
        
        return [totalPaths, maxAdventure]

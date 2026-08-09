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

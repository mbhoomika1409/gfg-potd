class Solution:
    def largestSquare(self, mat, queries, k):
        n = len(mat)
        m = len(mat[0])

        # Build 2D Prefix Sum
        prefix = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        # Get number of 1s in a rectangle
        def get_sum(r1, c1, r2, c2):
            return (
                prefix[r2 + 1][c2 + 1]
                - prefix[r1][c2 + 1]
                - prefix[r2 + 1][c1]
                + prefix[r1][c1]
            )

        answer = []

        for i, j in queries:

            # Maximum possible radius
            max_radius = min(
                i,
                j,
                n - 1 - i,
                m - 1 - j
            )

            # Check 1 x 1 square
            if mat[i][j] > k:
                answer.append(-1)
                continue

            low = 0
            high = max_radius
            best = 0

            # Binary search for largest valid radius
            while low <= high:
                mid = (low + high) // 2

                r1 = i - mid
                c1 = j - mid
                r2 = i + mid
                c2 = j + mid

                ones = get_sum(r1, c1, r2, c2)

                if ones <= k:
                    best = mid
                    low = mid + 1
                else:
                    high = mid - 1

            # Radius r gives side length 2*r + 1
            answer.append(2 * best + 1)

        return answer

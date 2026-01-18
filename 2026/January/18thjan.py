# Question:
# A k x k magic square is a k x k grid filled with integers such that:
# - Every row sum is equal
# - Every column sum is equal
# - Both diagonal sums are equal
#
# A 1 x 1 grid is always a magic square.
#
# Given an m x n integer grid, return the size (side length k)
# of the largest magic square that exists in the grid.

class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Prefix sums for rows and columns
        row_ps = [[0] * (n + 1) for _ in range(m)]
        col_ps = [[0] * n for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row_ps[i][j + 1] = row_ps[i][j] + grid[i][j]
                col_ps[i + 1][j] = col_ps[i][j] + grid[i][j]

        # Try square sizes from largest to smallest
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):

                    target = row_ps[i][j + k] - row_ps[i][j]
                    valid = True

                    # Check all rows
                    for r in range(i, i + k):
                        if row_ps[r][j + k] - row_ps[r][j] != target:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Check all columns
                    for c in range(j, j + k):
                        if col_ps[i + k][c] - col_ps[i][c] != target:
                            valid = False
                            break

                    if not valid:
                        continue

                    # Check both diagonals
                    diag1 = 0
                    diag2 = 0
                    for d in range(k):
                        diag1 += grid[i + d][j + d]
                        diag2 += grid[i + d][j + k - 1 - d]

                    if diag1 == target and diag2 == target:
                        return k

        return 1


# Explanation:
# - Any single cell is a valid 1x1 magic square.
# - We use prefix sums to compute row and column sums in O(1).
# - We try all square sizes starting from the largest possible.
# - For each k x k subgrid:
#     - All row sums must match.
#     - All column sums must match.
#     - Both diagonals must match the same sum.
# - The first valid square found (largest k) is returned.
#
# Time Complexity: O(min(m, n)^3)
# Space Complexity: O(m * n)
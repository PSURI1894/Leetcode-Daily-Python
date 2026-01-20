# Question:
# Given an m x n matrix mat and an integer threshold,
# return the maximum side length of a square such that the sum of all elements
# inside the square is less than or equal to threshold.
# If no such square exists, return 0.

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Build prefix sum matrix where
        # ps[i][j] = sum of submatrix from (0,0) to (i-1,j-1)
        ps = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                ps[i + 1][j + 1] = (
                    mat[i][j]
                    + ps[i][j + 1]
                    + ps[i + 1][j]
                    - ps[i][j]
                )

        # Helper function to get sum of k x k square
        # with top-left corner at (r, c)
        def square_sum(r, c, k):
            return (
                ps[r + k][c + k]
                - ps[r][c + k]
                - ps[r + k][c]
                + ps[r][c]
            )

        left, right = 0, min(m, n)
        ans = 0

        # Binary search on side length
        while left <= right:
            mid = (left + right) // 2
            found = False

            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if square_sum(i, j, mid) <= threshold:
                        found = True
                        break
                if found:
                    break

            if found:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

# Explanation:
# - We use a 2D prefix sum matrix to compute any sub-square sum in O(1).
# - The problem asks for the maximum side length, which is monotonic:
#   if a square of size k works, all smaller sizes also work.
# - This allows binary search on the side length.
# - For each candidate side length k, we check all possible k x k squares
#   and see if any has sum <= threshold.
# - The largest valid k found during binary search is the answer.
#
# Time Complexity: O(m * n * log(min(m, n)))
# Space Complexity: O(m * n)

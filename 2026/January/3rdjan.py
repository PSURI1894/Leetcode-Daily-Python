# Question:
# You have a grid of size n x 3 and you want to paint each cell of the grid
# with exactly one of the three colors: Red, Yellow, or Green.
# You must ensure that no two adjacent cells (horizontal or vertical)
# have the same color.
#
# Given n, return the number of ways to paint the grid.
# Since the answer can be very large, return it modulo 10^9 + 7.


class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        # aba: patterns like R G R (first and third same)
        # abc: patterns like R G B (all different)
        aba = 6  # 3 * 2
        abc = 6  # 3 * 2 * 1

        for _ in range(2, n + 1):
            new_aba = (aba * 3 + abc * 2) % MOD
            new_abc = (aba * 2 + abc * 2) % MOD

            aba = new_aba
            abc = new_abc

        return (aba + abc) % MOD


# Explanation:
# Each row of the grid can only be painted in two valid pattern types:
#
# 1) aba pattern:
#    The first and third cells have the same color, and the middle is different.
#    Example: Red-Green-Red
#
# 2) abc pattern:
#    All three cells have different colors.
#    Example: Red-Green-Yellow
#
# For the first row:
# aba = 6 ways
# abc = 6 ways
#
# For every subsequent row:
# - A new aba row can be formed from:
#     previous aba rows in 3 ways
#     previous abc rows in 2 ways
# - A new abc row can be formed from:
#     previous aba rows in 2 ways
#     previous abc rows in 2 ways
#
# We use dynamic programming and only keep track of the previous row counts,
# which gives us constant space usage.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

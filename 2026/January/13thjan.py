# Question:
# You are given a 2D integer array squares where squares[i] = [xi, yi, li]
# represents a square with bottom-left corner (xi, yi) and side length li.
# All squares are axis-aligned.
#
# Find the minimum y-coordinate of a horizontal line such that
# the total area of the squares strictly above the line
# equals the total area of the squares strictly below the line.
#
# Squares may overlap, and overlapping areas should be counted multiple times.
# Answers within 1e-5 of the correct value are accepted.


class Solution:
    def separateSquares(self, squares):
        # Function to compute (area_above - area_below) for a given y
        def balance(y):
            diff = 0.0
            for x, y0, l in squares:
                bottom = y0
                top = y0 + l
                area = l * l

                if y <= bottom:
                    # Entire square is above the line
                    diff += area
                elif y >= top:
                    # Entire square is below the line
                    diff -= area
                else:
                    # Line cuts the square
                    above = (top - y) * l
                    below = (y - bottom) * l
                    diff += above - below
            return diff

        # Binary search range for y
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        # Binary search to find y where balance(y) == 0
        for _ in range(60):  # enough iterations for 1e-5 precision
            mid = (low + high) / 2
            if balance(mid) > 0:
                low = mid
            else:
                high = mid

        return low


# Explanation:
# We are looking for a horizontal line y = c such that:
#   total area above the line = total area below the line
#
# Key idea:
# Define a function f(c) = (area above y=c) - (area below y=c).
# We want to find c such that f(c) = 0.
#
# For a single square:
# - If the line is completely below the square → full area is above
# - If the line is completely above the square → full area is below
# - If the line cuts the square → split area proportionally
#
# Since f(c) is a continuous and strictly decreasing function of c,
# we can use binary search on y.
#
# Steps:
# 1) Define balance(y) to compute area_above - area_below.
# 2) Binary search y between the minimum bottom and maximum top of all squares.
# 3) Stop after sufficient iterations to guarantee precision.
#
# Time Complexity:
# O(n * log(precision))
#
# Space Complexity:
# O(1)

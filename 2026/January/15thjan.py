# Question:
# You are given two integers n and m and two integer arrays hBars and vBars.
# The grid has (n + 2) horizontal bars and (m + 2) vertical bars, creating 1x1 unit cells.
#
# You can remove some bars from hBars (horizontal) and vBars (vertical).
# Other bars are fixed and cannot be removed.
#
# After removing bars, holes (empty regions) are formed.
# Return the maximum possible area of a square-shaped hole in the grid.


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars, vBars) -> int:
        # Sort the removable bars
        hBars.sort()
        vBars.sort()

        # Find the longest consecutive sequence in hBars
        max_h = 1
        curr = 1
        for i in range(1, len(hBars)):
            if hBars[i] == hBars[i - 1] + 1:
                curr += 1
            else:
                curr = 1
            max_h = max(max_h, curr)

        # Find the longest consecutive sequence in vBars
        max_v = 1
        curr = 1
        for i in range(1, len(vBars)):
            if vBars[i] == vBars[i - 1] + 1:
                curr += 1
            else:
                curr = 1
            max_v = max(max_v, curr)

        # Side length of the largest square hole
        side = min(max_h + 1, max_v + 1)

        return side * side


# Explanation:
# Each time we remove k consecutive horizontal bars,
# we merge (k + 1) rows into a single vertical span.
#
# Similarly, removing k consecutive vertical bars
# merges (k + 1) columns into a single horizontal span.
#
# To form a square hole:
# - Height = longest consecutive removed horizontal bars + 1
# - Width  = longest consecutive removed vertical bars + 1
#
# The largest possible square side length is:
# min(height, width)
#
# The answer is the area of that square: side²
#
# Key idea:
# This reduces to finding the longest consecutive sequence
# in hBars and vBars.
#
# Time Complexity:
# O(h log h + v log v) due to sorting
#
# Space Complexity:
# O(1)

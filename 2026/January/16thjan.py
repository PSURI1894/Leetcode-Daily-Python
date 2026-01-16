# Question:
# There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n).
# The field contains some horizontal fences given in hFences
# and some vertical fences given in vFences.
#
# You can remove some of these fences (possibly none).
# The outer boundary fences of the field cannot be removed.
#
# After removing fences, the field is divided into rectangles.
# Return the maximum possible area of a square field that can be formed.
# If it is impossible to form a square, return -1.
#
# Since the answer may be large, return it modulo 10^9 + 7.


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences, vFences) -> int:
        MOD = 10**9 + 7

        # Add boundary fences
        h = [1] + hFences + [m]
        v = [1] + vFences + [n]

        # Sort fence positions
        h.sort()
        v.sort()

        # Compute all possible heights
        heights = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                heights.add(h[j] - h[i])

        # Compute all possible widths and check for square
        max_side = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                width = v[j] - v[i]
                if width in heights:
                    max_side = max(max_side, width)

        if max_side == 0:
            return -1

        return (max_side * max_side) % MOD


# Explanation:
# The fences divide the field into smaller rectangles.
# A square can be formed if:
#   (difference between two horizontal fences)
#   ==
#   (difference between two vertical fences)
#
# Steps:
# 1. Add the boundary fences at positions 1 and m (horizontal),
#    and 1 and n (vertical), because they cannot be removed.
# 2. Sort the fence positions.
# 3. Compute all possible vertical distances (heights) between pairs
#    of horizontal fences.
# 4. Compute all possible horizontal distances (widths) between pairs
#    of vertical fences.
# 5. Find the maximum distance that appears in both sets.
#    That distance is the side of the largest square.
#
# If no common distance exists, forming a square is impossible.
#
# Time Complexity:
# O(H^2 + V^2), where H = len(hFences), V = len(vFences)
# (acceptable since constraints are small, ≤ 600)
#
# Space Complexity:
# O(H^2) for storing possible heights

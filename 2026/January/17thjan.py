# Question:
# You are given multiple axis-aligned rectangles on a 2D plane.
# Each rectangle is defined by its bottom-left and top-right coordinates.
#
# You must find the maximum possible area of a square that can be placed
# completely inside the intersection region of at least two rectangles.
#
# If no two rectangles intersect, return 0.

class Solution:
    def largestSquareArea(self, bottomLeft: list[list[int]], topRight: list[list[int]]) -> int:
        n = len(bottomLeft)
        max_area = 0

        # Check intersection for every pair of rectangles
        for i in range(n):
            for j in range(i + 1, n):
                left = max(bottomLeft[i][0], bottomLeft[j][0])
                bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                right = min(topRight[i][0], topRight[j][0])
                top = min(topRight[i][1], topRight[j][1])

                # If intersection exists
                if right > left and top > bottom:
                    side = min(right - left, top - bottom)
                    max_area = max(max_area, side * side)

        return max_area


# Explanation:
# - A square can only fit inside the overlapping region of two rectangles.
# - For every pair of rectangles, we compute their intersection.
# - The largest square that fits inside an intersection has side length:
#       min(intersection width, intersection height)
# - We compute the square area for each valid intersection and track the maximum.
# - If no rectangles overlap, the result remains 0.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

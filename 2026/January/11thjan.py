# Question:
# Given a rows x cols binary matrix filled with '0's and '1's,
# find the largest rectangle containing only '1's and return its area.
#
# Each rectangle must be made up entirely of contiguous '1's.


class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            # Build histogram heights for this row
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            # Calculate max rectangle area in histogram
            stack = []
            for i in range(cols + 1):
                curr_height = heights[i] if i < cols else 0

                while stack and curr_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area


# Explanation:
# This problem is reduced to the "Largest Rectangle in Histogram" problem.
#
# Key idea:
# Treat each row as the base of a histogram where:
# - heights[j] = number of consecutive '1's above (and including) current row in column j
#
# For each row:
# 1) Update the histogram heights.
# 2) Compute the largest rectangle in the histogram using a monotonic stack.
#
# Stack logic:
# - The stack keeps indices of increasing bar heights.
# - When a smaller height is encountered, we pop from the stack and calculate
#   rectangle areas using the popped height as the limiting factor.
#
# A sentinel (extra 0 height) is added at the end to flush the stack.
#
# Time Complexity:
# O(rows * cols)
#
# Space Complexity:
# O(cols)
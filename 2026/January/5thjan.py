# Question:
# You are given an n x n integer matrix.
# You can perform the following operation any number of times:
# - Choose any two adjacent elements of the matrix and multiply each of them by -1.
#   (Two elements are adjacent if they share a border.)
#
# Your goal is to maximize the sum of the matrix's elements.
# Return the maximum possible sum after applying the operations optimally.


class Solution:
    def maxMatrixSum(self, matrix):
        total_sum = 0
        min_abs = float('inf')
        negative_count = 0

        for row in matrix:
            for val in row:
                total_sum += abs(val)
                min_abs = min(min_abs, abs(val))
                if val < 0:
                    negative_count += 1

        # If the number of negative elements is even,
        # we can make all values positive
        if negative_count % 2 == 0:
            return total_sum

        # If odd, one smallest absolute value must stay negative
        return total_sum - 2 * min_abs


# Explanation:
# The key insight is that flipping two adjacent elements changes the sign of both,
# which means the parity (even/odd) of the total number of negative elements
# never changes.
#
# Strategy:
# 1) Take the absolute value of all elements — this is the best possible contribution.
# 2) Count how many negative numbers exist.
# 3) Track the smallest absolute value in the matrix.
#
# If the number of negative elements is even:
# - We can pairwise flip negatives and make all values positive.
# - The answer is simply the sum of absolute values.
#
# If the number of negative elements is odd:
# - One element must remain negative.
# - To minimize loss, we keep the smallest absolute value negative.
# - So we subtract twice that smallest value from the total sum.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Question:
# Given two integer arrays nums1 and nums2.
#
# Return the maximum dot product between non-empty subsequences of nums1 and nums2
# that have the same length.
#
# A subsequence is formed by deleting some (or none) elements without changing
# the order of the remaining elements.
#
# The dot product of two arrays of equal length is the sum of the products of
# corresponding elements.


class Solution:
    def maxDotProduct(self, nums1, nums2):
        n, m = len(nums1), len(nums2)

        # dp[i][j] = maximum dot product using nums1[i:] and nums2[j:]
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                product = nums1[i] * nums2[j]

                # Three choices:
                # 1) Take nums1[i] and nums2[j] together
                # 2) Skip nums1[i]
                # 3) Skip nums2[j]
                dp[i][j] = max(
                    product,
                    product + max(0, dp[i + 1][j + 1]),
                    dp[i + 1][j],
                    dp[i][j + 1]
                )

        return dp[0][0]


# Explanation:
# This is a Dynamic Programming problem where we must choose matching subsequences
# from both arrays to maximize their dot product.
#
# Key challenge:
# - Subsequences must be non-empty
# - Values can be negative, so we cannot default to 0 everywhere
#
# State Definition:
# dp[i][j] represents the maximum dot product we can get using
# elements from nums1[i:] and nums2[j:].
#
# Transitions:
# At each position (i, j), we have three options:
#
# 1) Pair nums1[i] with nums2[j]:
#    - Start a new subsequence: nums1[i] * nums2[j]
#    - Or extend an existing subsequence: nums1[i] * nums2[j] + dp[i+1][j+1]
#
# 2) Skip nums1[i]:
#    dp[i+1][j]
#
# 3) Skip nums2[j]:
#    dp[i][j+1]
#
# We take the maximum of these choices.
#
# The use of max(0, dp[i+1][j+1]) ensures we only extend subsequences
# when it increases the value, which correctly handles negative values.
#
# Final Answer:
# dp[0][0] gives the maximum dot product using the full arrays.
#
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

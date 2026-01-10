# Question:
# Given two strings s1 and s2, return the minimum ASCII sum of deleted characters
# required to make the two strings equal.
#
# You may delete characters from either string.
# The cost of deleting a character is its ASCII value.
#
# The goal is to minimize the total deletion cost.


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        # dp[i][j] = minimum ASCII delete sum to make s1[i:] and s2[j:] equal
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Base case: delete all remaining characters from s1
        for i in range(n - 1, -1, -1):
            dp[i][m] = dp[i + 1][m] + ord(s1[i])

        # Base case: delete all remaining characters from s2
        for j in range(m - 1, -1, -1):
            dp[n][j] = dp[n][j + 1] + ord(s2[j])

        # Fill the DP table
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        ord(s1[i]) + dp[i + 1][j],
                        ord(s2[j]) + dp[i][j + 1]
                    )

        return dp[0][0]


# Explanation:
# This is a Dynamic Programming problem similar to Longest Common Subsequence,
# but instead of maximizing length, we minimize deletion cost.
#
# State:
# dp[i][j] represents the minimum ASCII delete sum needed to make
# substrings s1[i:] and s2[j:] equal.
#
# Transitions:
# - If s1[i] == s2[j]:
#   No deletion needed for these characters, move both pointers forward.
#
# - If s1[i] != s2[j]:
#   We have two choices:
#   1) Delete s1[i] → cost = ASCII(s1[i]) + dp[i+1][j]
#   2) Delete s2[j] → cost = ASCII(s2[j]) + dp[i][j+1]
#   Take the minimum of the two.
#
# Base Cases:
# - If one string is exhausted, delete all remaining characters
#   from the other string.
#
# Final Answer:
# dp[0][0] gives the minimum ASCII delete sum for the full strings.
#
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
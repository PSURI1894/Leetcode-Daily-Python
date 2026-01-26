# Question:
# 1200. Minimum Absolute Difference
#
# Given an array of distinct integers arr, find all pairs of elements
# with the minimum absolute difference between any two elements.
#
# Return the list of pairs in ascending order.
# Each pair [a, b] satisfies:
# - a < b
# - b - a equals the minimum absolute difference.

from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Step 1: Sort the array
        arr.sort()

        # Step 2: Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i - 1])

        # Step 3: Collect all pairs with this minimum difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == min_diff:
                result.append([arr[i - 1], arr[i]])

        return result


# Explanation:
#
# Key Insight:
# After sorting the array, the minimum absolute difference
# must occur between adjacent elements.
#
# Why this works:
# - If two elements are not adjacent in sorted order,
#   at least one number lies between them, making the difference larger.
#
# Algorithm:
# 1. Sort the array.
# 2. Scan once to find the minimum difference.
# 3. Scan again to collect all adjacent pairs with that difference.
#
# Example:
# arr = [4,2,1,3]
# Sorted = [1,2,3,4]
# Minimum difference = 1
# Result = [[1,2],[2,3],[3,4]]
#
# Time Complexity: O(n log n)
# Space Complexity: O(1) extra space (excluding output)
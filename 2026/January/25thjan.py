# Question:
# 1984. Minimum Difference Between Highest and Lowest of K Scores
#
# You are given an integer array nums where nums[i] represents the score
# of the i-th student, and an integer k.
#
# Pick scores of any k students such that the difference between the
# highest and the lowest of the k scores is minimized.
#
# Return the minimum possible difference.

from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # If only one score is chosen, difference is zero
        if k == 1:
            return 0
        
        # Sort the scores
        nums.sort()
        
        ans = float('inf')
        n = len(nums)
        
        # Sliding window of size k
        for i in range(n - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        
        return ans


# Explanation:
#
# Key Insight:
# To minimize (max - min) among k selected elements, we should choose
# elements that are as close to each other as possible.
#
# Why sorting works:
# - After sorting, any group of k elements with minimal difference
#   must be contiguous.
# - Any non-contiguous selection would only increase the range.
#
# Algorithm:
# 1. Sort nums
# 2. Use a sliding window of length k
# 3. For each window, compute:
#       difference = nums[i + k - 1] - nums[i]
# 4. Track the minimum difference
#
# Example:
# nums = [9,4,1,7], k = 2
# Sorted nums = [1,4,7,9]
#
# Windows:
# [1,4] -> diff = 3
# [4,7] -> diff = 3
# [7,9] -> diff = 2  (minimum)
#
# Output = 2
#
# Time Complexity: O(n log n)
# Space Complexity: O(1) extra space

# Question:
# 1877. Minimize Maximum Pair Sum in Array
#
# The pair sum of a pair (a, b) is a + b.
# Given an array nums of even length n, pair up the elements into n/2 pairs such that:
# - Each element is used exactly once
# - The maximum pair sum is minimized
#
# Return the minimized maximum pair sum after optimal pairing.


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # Sort the array so we can apply a greedy pairing strategy
        nums.sort()

        left = 0
        right = len(nums) - 1
        max_pair_sum = 0

        # Pair the smallest and largest elements
        while left < right:
            max_pair_sum = max(max_pair_sum, nums[left] + nums[right])
            left += 1
            right -= 1

        return max_pair_sum


# Explanation:
#
# Key Idea:
# To minimize the maximum pair sum, we must avoid pairing large numbers together.
# The optimal strategy is to:
#   - Sort the array
#   - Pair the smallest element with the largest
#
# Why this works:
# - If large numbers are paired together, the pair sum becomes large.
# - Pairing the smallest with the largest balances the sums across all pairs.
#
# Example:
# nums = [3,5,2,3]
# Sorted = [2,3,3,5]
# Pairs:
#   (2,5) -> 7
#   (3,3) -> 6
# Maximum pair sum = 7 (minimum possible)
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) extra space (ignoring sorting internals)
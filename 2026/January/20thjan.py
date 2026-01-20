# Question:
# You are given an array nums consisting of n prime integers.
#
# Construct an array ans of length n such that for every index i:
#     ans[i] OR (ans[i] + 1) == nums[i]
#
# Among all possible values, ans[i] should be minimized.
# If it is not possible to find such a value, set ans[i] = -1.
#
# Return the resulting array ans.

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []

        for x in nums:
            value = -1

            # Try all possible candidates starting from the smallest
            # ans[i] must be strictly less than nums[i]
            for a in range(x):
                if (a | (a + 1)) == x:
                    value = a
                    break

            result.append(value)

        return result

# Explanation:
# - For each prime number x in nums, we need to find the smallest integer a
#   such that a OR (a + 1) equals x.
# - The bitwise OR operation can only set bits, never unset them,
#   so a must be smaller than x.
# - We brute-force all values a from 0 to x - 1 and check the condition.
# - The first valid a found is the minimum possible value, so we select it.
# - If no value satisfies the condition, we return -1 for that position.
#
# Constraints are small (nums[i] ≤ 1000), so brute force is efficient.
#
# Time Complexity:
# O(n * max(nums))
#
# Space Complexity:
# O(n)

# Question:
# You are given an array nums consisting of n prime integers.
#
# Construct an array ans of length n such that for each index i:
#     ans[i] OR (ans[i] + 1) == nums[i]
#
# You must minimize ans[i]. If it is not possible, set ans[i] = -1.
#
# Return the resulting array ans.

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []

        for x in nums:
            # If x is even, impossible
            if x % 2 == 0:
                ans.append(-1)
                continue

            # Count trailing 1s in binary representation of x
            t = 0
            while ((x >> t) & 1) == 1:
                t += 1

            # Remove the highest bit among trailing 1s
            ans.append(x - (1 << (t - 1)))

        return ans


# Explanation:
# - For a value x to satisfy a OR (a + 1) = x, x must be odd.
#   If x is even, no such a exists.
#
# - Let x have k trailing 1s in binary.
#   Example: x = 101111  (k = 4)
#
# - The smallest possible a is obtained by turning the highest trailing 1 to 0:
#       a = x - 2^(k-1)
#
# - This guarantees:
#       a OR (a + 1) == x
#   and ensures a is minimized.
#
# - We apply this logic independently for each element.
#
# Time Complexity:
# O(n · log(nums[i]))
#
# Space Complexity:
# O(n)

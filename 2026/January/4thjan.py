# Question:
# You are given an integer array nums.
# Return the sum of divisors of the integers in nums that have exactly four divisors.
# If no such integer exists, return 0.
#
# Example:
# nums = [21, 4, 7]
# 21 has divisors: 1, 3, 7, 21 → exactly 4 divisors → sum = 32
# 4 has 3 divisors, 7 has 2 divisors → ignored
# Answer = 32


class Solution:
    def sumFourDivisors(self, nums):
        total_sum = 0

        for num in nums:
            count = 0
            div_sum = 0

            i = 1
            while i * i <= num:
                if num % i == 0:
                    d1 = i
                    d2 = num // i

                    if d1 == d2:
                        count += 1
                        div_sum += d1
                    else:
                        count += 2
                        div_sum += d1 + d2

                    if count > 4:
                        break
                i += 1

            if count == 4:
                total_sum += div_sum

        return total_sum


# Explanation:
# We iterate through each number in the array and count its divisors.
# For each divisor i up to sqrt(num), there is a paired divisor num // i.
#
# If both divisors are equal (perfect square), we count it once.
# Otherwise, we count two divisors at a time.
#
# If the number of divisors exceeds 4, we stop early to save time.
# Only numbers with exactly 4 divisors contribute their divisor sum.
#
# Time Complexity:
# O(n * sqrt(max(nums[i])))
#
# Space Complexity:
# O(1)

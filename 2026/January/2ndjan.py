# Question:
# You are given an integer array nums with the following properties:
# 1) nums.length = 2 * n
# 2) nums contains n + 1 unique elements
# 3) Exactly one element in nums is repeated n times
#
# Return the element that is repeated n times.


class Solution:
    def repeatedNTimes(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen:
                return num
            seen.add(num)


# Explanation:
# The key observation is that only one element is repeated multiple times,
# while all other elements appear exactly once.
#
# We iterate through the array and keep track of elements we have already seen
# using a set.
# If we encounter an element that already exists in the set, that element
# must be the one repeated n times, so we return it immediately.
#
# This works because the repeated element will appear again before all
# unique elements are exhausted.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

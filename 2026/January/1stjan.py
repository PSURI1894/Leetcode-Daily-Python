# Question:
# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant.
# The integer does not contain any leading zeros.
#
# Increment the large integer by one and return the resulting array of digits.


class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from the last digit and move left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9, we need an extra digit at the front
        return [1] + digits


# Explanation:
# We simulate how addition works in real life.
# Starting from the last digit, we try to add 1.
# If the digit is less than 9, we can increment it and stop.
# If the digit is 9, it becomes 0 and we carry the 1 to the next digit on the left.
# If all digits are 9 (e.g., [9,9,9]), the result becomes [1,0,0,0].
# This approach avoids converting the array into an integer and works efficiently
# in O(n) time with O(1) extra space (excluding the output array).

# Question:
# Given two binary strings a and b, return their sum as a binary string.
#
# Each string consists only of '0' and '1'.
# The result should be returned without leading zeros (unless the result is "0").

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        # Traverse both strings from right to left
        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += ord(a[i]) - ord('0')
                i -= 1

            if j >= 0:
                total += ord(b[j]) - ord('0')
                j -= 1

            # Current binary digit
            result.append(str(total % 2))

            # Update carry
            carry = total // 2

        # Reverse since we built the number from LSB to MSB
        return ''.join(reversed(result))


"""
Explanation:
- Binary addition is performed from right to left (least significant bit first).
- At each step, add the two bits and the carry.
- The resulting bit is total % 2.
- Carry is total // 2.
- Continue until both strings are exhausted and carry is zero.
- Reverse the collected bits to form the final binary string.

Time Complexity:
O(max(len(a), len(b)))

Space Complexity:
O(max(len(a), len(b)))
"""

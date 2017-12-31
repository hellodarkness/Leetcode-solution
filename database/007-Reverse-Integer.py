# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output:  321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        digits = []
        if x == 0:
            return 0

        remains = abs(x)
        sign = -1 if x < 0 else 1

        while (True):
            # remains is not zero
            digit = remains % 10
            remains = (remains - digit) / 10
            digits.append(digit)
            if remains == 0:
                break

        ret = 0
        for i in digits:
            ret *= 10
            ret += i

        ret *= sign
        if abs(ret) > 0x7FFFFFFF:
            return 0
        else:
            return ret

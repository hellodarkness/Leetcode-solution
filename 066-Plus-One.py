# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        c = 0
        list = []

        for n in digits[:: -1]:
            list.append((c + n) % 10)
            c = (c + n) // 10

        if c > 0:
            list.append(c)

        return list[:: -1]


# Determine whether an integer is a palindrome. Do this without extra space.

class Solution(object):
    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        if x < 10:
            return True

        reversednum = 0
        while x > reversednum:
            reversednum = reversednum * 10 + x % 10
            x /= 10

        return x == reversednum or x == reversednum / 10

# O(log10^n)

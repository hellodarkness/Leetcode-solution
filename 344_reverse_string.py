//Write a function that takes a string as input and returns the string reversed.

class Solution(object):
    def reverseString(self, s):
        return s[::-1]
s=Solution()
print(s.reverseString("hello"))

class Solution2(object):
    def reverseString(self, s):
        r = list(s)
        i, j  = 0, len(r) - 1
        while i < j:
            r[i], r[j] = r[j], r[i]
            i += 1
            j -= 1
        return "".join(r)
s=Solution2()
print(s.reverseString("hello"))
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
# For example,"A man, a plan, a canal: Panama" is a palindrome."race a car" is not a palindrome.

class Solution(object):
    def isPalindrome(self, s):
        import re
        if len(s) < 2:
            return True
        s = re.sub(r'\W+','', s).replace(' ', '').lower()

# why `s = [c.lower() for c in s if c.isalnum()]` is wrong here

        string = list(s)
        i = 0
        j = (len(s) - 1)
        while i < j:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
        return (s == ''.join(string))
s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))

class Solution(object):
    def isPalindrome(self, s):
        s=[c.lower() for c in s if c.isalnum()]
        return s == s[::-1]
s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))



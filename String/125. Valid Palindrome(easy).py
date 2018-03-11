# -*- coding: utf-8 -*-

'''
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty?
This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class ReSolution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def check_alpha_numeric(c):
            return c.isalpha() or c.isdigit()
        array = []
        for i in range(len(s)):
            if check_alpha_numeric(s[i]):
                array.append(s[i].lower())
        return array == array[::-1]

re = ReSolution()
print re.isPalindrome("A man, a plan, a canal: Panama")

class Solution(object):
    def isPalindromeMy(self, s):
        """
        :type s: str
        :rtype: bool
        """
        array = []
        for i in range(len(s)):
            if self.checkAlphanumeric(s[i]) and s[i].isalpha():
                array.append(s[i].lower())
            elif self.checkAlphanumeric(s[i]) and s[i].isdigit():
                array.append(s[i])
        return array == array[::-1]

    def checkAlphanumeric(self, c):
        # ord_a = ord('a')
        # ord_z = ord('z')
        # ord_A = ord('A')
        # ord_Z = ord('Z')
        # ord_value = ord(c)
        # return ord_a <= ord_value <= ord_z or ord_A <= ord_value <= ord_Z
        return c.isalpha() or c.isdigit()


solu = Solution()
print solu.isPalindromeMy('0P')
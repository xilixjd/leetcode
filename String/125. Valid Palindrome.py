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
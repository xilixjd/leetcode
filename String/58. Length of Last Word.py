# -*- coding: utf-8 -*-

'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''


class Solution(object):
    def lengthOfLastWordMy(self, s):
        """
        :type s: str
        :rtype: int
        """
        array = s.split(' ')
        for i in range(len(array))[::-1]:
            if len(array[i]) != 0:
                return len(array[i])

        return 0

solu = Solution()
print solu.lengthOfLastWordMy("a ")
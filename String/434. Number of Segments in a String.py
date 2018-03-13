# -*- coding: utf-8 -*-
'''
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:

Input: "Hello, my name is John"
Output: 5
'''

class Solution(object):
    def countSegments(self, s):
        """
        感觉没啥意思 这个题
        :type s: str
        :rtype: int
        """
        # if len(s) == 0:
        #     return 0
        # count = 1
        # temp_sig = False
        # for i in range(1, len(s) - 1):
        #     if not s[i].isalpha() and temp_sig:
        #         # if not s[i-1].isalpha() and not s[i+1].isalpha():
        #         #     continue
        #         # print i
        #         temp_sig = False
        #         count += 1
        #     if s[i].isalpha():
        #         temp_sig = True
        # return count
        return len(s.split())

    def countSegments2(self, s):
        count = 0
        for i in range(len(s)):
            if s[i] != ' ' and (i == 0 or s[i-1] == ' '):
                count += 1
        return count


solu = Solution()

print solu.countSegments2(' ')
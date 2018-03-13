# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

'''


class Solution(object):
    def firstUniqChar1(self, s):
        """
        思路1：暴力法，双循环
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            c = s[i]
            flag = False
            for j in range(len(s)):
                if j != i and c == s[j]:
                    flag = True
                    break
            if not flag:
                return i
        return -1

    def firstUniqChar2(self, s):
        record_dict = {}
        for i in range(len(s)):
            if record_dict.get(s[i]) is None:
                record_dict[s[i]] = 1
            else:
                record_dict[s[i]] += 1
        for i in range(len(s)):
            if record_dict[s[i]] == 1:
                return i
        return -1

sl = Solution()
print sl.firstUniqChar2("cc")
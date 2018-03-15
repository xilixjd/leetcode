# -*- coding: utf-8 -*-
'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
'''

class ReSolution(object):
    def repeatedSubstringPattern1(self, s):
        """
        思路1：
        超时
        :type s: str
        :rtype: bool
        """
        def check_empty_str_array(array):
            for a in array:
                if len(a) > 0:
                    return False
            return True

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                temp_str = s[i: j]
                temp_array = s.split(temp_str)
                if check_empty_str_array(temp_array):
                    return True
        return False

    def repeatedSubstringPattern2(self, s):
        """
        思路2：
        :type s: str
        :rtype: bool
        """
        length = len(s)
        for i in range(1, len(s) / 2 + 1):
            print i
            if length % i == 0 and s[: i] * (length / i) == s:
                return True
        return False

re = ReSolution()
print re.repeatedSubstringPattern2("aaaa")


class Solution(object):
    def repeatedSubstringPatternMy(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s) - 1):
            if len(s) % (i+1) == 0 and s[:i+1] * (len(s) / (i+1)) == s:
                return True
        return False

solu = Solution()
print solu.repeatedSubstringPatternMy('abcabcabcab')
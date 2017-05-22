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
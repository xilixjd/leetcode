# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        中文版通过了
        :type s: str
        :rtype: str
        """
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        max_str = s[0]
        max_length = 1
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_length = 2
                max_str = s[i: i + 2]
        for length in range(2, len(dp) + 1):
            for i in range(len(dp) - 2):
                j = i + length
                if j < len(dp) and dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if j + 1 - i > max_length:
                        max_length = j + 1 - i
                        max_str = s[i: j + 1]
        return max_str

solu = Solution()
print solu.longestPalindrome("abccb")

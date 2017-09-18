# -*- coding: utf-8 -*-

'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string
which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''


class Solution(object):
    def numDistinct(self, s, t):
        """
        这篇文章讲的不错
        http://blog.csdn.net/feliciafay/article/details/42959119
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
        dp[0][0] = 1
        for i in range(1, len(s)):
            dp[0][i] = 1
        for i in range(1, len(t)):
            dp[i][0] = 0
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                dp[i][j] = dp[i][j-1]
                if s[j-1] == t[i-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[len(t)][len(s)]

solu = Solution()
print solu.numDistinct('ABCDE', 'ACE')
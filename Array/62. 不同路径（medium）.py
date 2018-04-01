# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''


class Solution(object):
    def uniquePaths(self, m, n):
        """
        自己写的
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][1] = 1
        for j in range(1, n + 1):
            dp[1][j] = 1
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[i][j]

solu = Solution()
print solu.uniquePaths(4, 3)
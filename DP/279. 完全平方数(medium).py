# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3 
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
'''
import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, len(dp)):
            min_dp = 100000000
            if math.sqrt(i) % 1 == 0:
                dp[i] = 1
                continue
            for j in range(1, i / 2 + 1):
                min_dp = min(min_dp, dp[j] + dp[i - j])
            dp[i] = min_dp
        # print dp
        return dp[n]

    def numSquares2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1000000 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, len(dp)):
            if math.sqrt(i) % 1 == 0:
                dp[i] = 1
                continue
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        # print dp
        return dp[n]

    def numSquares3(self, n):
        dp = [1000000 for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]

solu = Solution()
print solu.numSquares3(7691)
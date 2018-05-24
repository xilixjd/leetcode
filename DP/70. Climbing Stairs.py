# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


class ReSolution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairsDP(self, n):
        if n == 1:
            return 1
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

solu = Solution()
re = ReSolution()
print re.climbStairsDP(1)
print solu.climbStairs(5)
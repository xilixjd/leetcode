# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

例如，给定 n = 2，返回1（2 = 1 + 1）；给定 n = 10，返回36（10 = 3 + 3 + 4）。

注意：你可以假设 n 不小于2且不大于58。

感谢：
特别感谢 @jianchao.li.fighter 添加此问题并创建所有测试用例。
'''


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 0
        dp[2] = 1
        for i in range(2, len(dp)):
            for j in range(1, i / 2 + 1):
                dp[i] = max(dp[i], max(j, dp[j]) * max(i - j, dp[i - j]))
        # print dp
        return dp[n]

solu = Solution()
print solu.integerBreak(10)
# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：

如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''


class Solution(object):
    def minimumTotal(self, triangle):
        """
        非 dp：做累加
        dp：思路类似，只是累加放在一个 dp 数组中
        自上而下
        :type triangle: List[List[int]]
        :rtype: int
        """
        if len(triangle) == 0:
            return
        if len(triangle[0]) == 0:
            return
        dp = [0 for i in range(len(triangle))]
        dp[0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i]))[::-1]:
                if j == 0:
                    dp[j] += triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[j] = dp[j - 1] + triangle[i][j]
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + triangle[i][j]
        return min(dp)

    def minimumTotal2(self, triangle):
        '''
        自下而上
        :param triangle:
        :return:
        '''
        dp = [[0 for i in range(len(triangle[len(triangle) - 1]))] for j in range(len(triangle))]
        for j in range(len(triangle[len(triangle) - 1])):
            dp[len(triangle) - 1][j] = triangle[len(triangle) - 1][j]
        for i in range(len(triangle) - 1)[::-1]:
            for j in range(i + 1):
                # dp[j]
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

solu = Solution()
print solu.minimumTotal2([[2],[8, 0],[1,9,10], [4,6,7,2]])
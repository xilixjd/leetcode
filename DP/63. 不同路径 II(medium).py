# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            dp[i + 1][1] = 1
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            dp[1][i + 1] = 1
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                print j
                if obstacleGrid[i - 1][j - 1] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m][n]

solu = Solution()
print solu.uniquePathsWithObstacles([[0],[0]])
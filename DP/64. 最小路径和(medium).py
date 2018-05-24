# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        row_sums = 0
        for i in range(m):
            row_sums += grid[i][0]
            dp[i][0] = row_sums
        col_sums = 0
        for i in range(n):
            col_sums += grid[0][i]
            dp[0][i] = col_sums
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]

solu = Solution()
print solu.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])
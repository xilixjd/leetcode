# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def sum_row(nums, row):
            sums = 0
            for i in range(row):
                sums += nums[i][0]
            return sums
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][1] = sum_row(grid, i)
        for j in range(1, n + 1):
            dp[1][j] = sum(grid[0][:j])
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]
        return dp[i][j]


solu = Solution()
print solu.minPathSum([[1,3,1],
 [1,5,1],
 [4,2,2]])
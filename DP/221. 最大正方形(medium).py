# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

'''


class Solution(object):
    def maximalSquare(self, matrix):
        """
        通过，速度有点慢
        :type matrix: List[List[str]]
        :rtype: int
        """
        def judge_squre(i, j, length, matrix):
            for x in range(i - length, i):
                if matrix[x][j] == "0":
                    return False
            for y in range(j - length, j):
                if matrix[i][y] == "0":
                    return False
            return True

        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        if len(matrix) == 1:
            for i in range(len(matrix[0])):
                if matrix[0][i] == "1":
                    return 1
            return 0
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                if matrix[i][0] == "1":
                    return 1
            return 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        max_square = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if matrix[i][j] == "1":
                    max_square = 1
                dp[i][j] = int(matrix[i][j])
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i][j] == "1" and dp[i - 1][j - 1] > 0:
                    squre_length = dp[i - 1][j - 1]
                    while not judge_squre(i, j, squre_length, matrix):
                        squre_length -= 1
                    dp[i][j] = squre_length + 1
                    max_square = max(max_square, dp[i][j] ** 2)
        # print dp
        return max_square

    def maximalSquare2(self, matrix):
        '''
        https://leetcode.com/problems/maximal-square/discuss/120219/DP-with-boundary-initialization-but-easier-to-understand
        '''
        pass

solu = Solution()
# print solu.maximalSquare([["0","0","0","1"],
#                           ["1","1","0","1"],
#                           ["1","1","1","1"],
#                           ["0","1","1","1"],
#                           ["0","1","1","1"]])
print solu.maximalSquare([["1"],["0"],["1"],["1"],["1"],["1"],["0"]])

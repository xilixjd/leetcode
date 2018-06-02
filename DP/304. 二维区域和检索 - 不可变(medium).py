# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。

Range Sum Query 2D
上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。

示例:

给定 matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
说明:

你可以假设矩阵不可变。
会多次调用 sumRegion方法。
你可以假设 row1 ≤ row2 且 col1 ≤ col2。
'''


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(self.dp)):
            temp = 0
            for j in range(len(self.dp[0])):
                temp += matrix[i][j]
                self.dp[i][j] = temp
        for d in self.dp:
            print d

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sums = 0
        for i in range(row1, row2 + 1):
            if col1 != 0:
                sums = sums + self.dp[i][col2] - self.dp[i][col1 - 1]
            else:
                sums = sums + self.dp[i][col2]
        return sums


class NumMatrix2(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(self.dp)):
            for j in range(len(self.dp[0])):
                left = self.dp[i][j - 1] if j > 0 else 0
                top = self.dp[i - 1][j] if i > 0 else 0
                top_left = self.dp[i - 1][j - 1] if j > 0 and i > 0 else 0
                self.dp[i][j] = matrix[i][j] + left + top - top_left
        print self.dp

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        rect_top = self.dp[row1 - 1][col2] if row1 > 0 else 0
        rect_left = self.dp[row2][col1 - 1] if col1 > 0 else 0
        rect_top_left = self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.dp[row2][col2] - rect_top - rect_left + rect_top_left


# Your NumMatrix object will be instantiated and called as such:
obj = NumMatrix2([
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
])
param_1 = obj.sumRegion(1,1,2,2)
print param_1
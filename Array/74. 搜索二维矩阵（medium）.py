# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''


class Solution(object):
    def searchMatrixMy(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = j = 0
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        while i < len(matrix):
            if i != len(matrix) - 1:
                if matrix[i][0] <= target < matrix[i + 1][0]:
                    j = 0
                    while j < len(matrix[0]):
                        if matrix[i][j] == target:
                            return True
                        j += 1
                    return False
            else:
                for n in matrix[i]:
                    if n == target:
                        return True
                return False
            i += 1
        return False

    def searchMatrix(self, matrix, target):
        '''
        二分
        :param matrix:
        :param target:
        :return:
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows * cols - 1
        while start <= end:
            mid = (start + end) / 2
            mid_val = matrix[mid / cols][mid % cols]
            if mid_val == target:
                return True
            elif mid_val < target:
                start = mid + 1
            else:
                end = mid - 1
        return False


solu = Solution()
print solu.searchMatrix([
  [1], [3]
], 3)
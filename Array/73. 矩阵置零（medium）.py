# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def set_zero(matrix, row, col):
            for i in range(len(matrix)):
                matrix[i][col] = 0
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

        row_col_dict = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row_col_dict[str([i, j])] = [i, j]
        for k in row_col_dict:
            row, col = row_col_dict[k]
            set_zero(matrix, row, col)
        print matrix

solu = Solution()
solu.setZeroes([[1,0,5], [2,0,6], [6,8,7]])
# -*- coding: utf-8 -*-
'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

import copy
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 0:
            return [[]]
        matrix_copy = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix_copy[n-j-1][i]
        print matrix

solu = Solution()
solu.rotate([[1,2,3],[4,5,6],[7,8,9]])
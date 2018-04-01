# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def scan(matrix, colomns, rows, start, iter):
            endX = colomns - 1 - start
            endY = rows - 1 - start
            for i in range(start, endX + 1):
                matrix[start][i] = iter
                iter += 1
            if start < endY:
                for i in range(start + 1, endY + 1):
                    matrix[i][endX] = iter
                    iter += 1
            if start < endX and start < endY:
                for i in range(start, endX)[::-1]:
                    matrix[endY][i] = iter
                    iter += 1
            if start < endX and start < endY - 1:
                for i in range(start + 1, endY)[::-1]:
                    matrix[i][start] = iter
                    iter += 1
            return iter

        start = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        iter = 1
        # 必须得 start * 2
        while start * 2 < n:
            iter = scan(matrix, len(matrix[0]), len(matrix), start, iter)
            start += 1
        return matrix


solu = Solution()
print solu.generateMatrix(0)
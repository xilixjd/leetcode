# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

''''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        def scan(matrix, colomns, rows, start, res):
            endX = colomns - 1 - start
            endY = rows - 1 - start
            for i in range(start, endX + 1):
                res.append(matrix[start][i])
            if start < endY:
                for i in range(start + 1, endY + 1):
                    res.append(matrix[i][endX])
            if start < endX and start < endY:
                for i in range(start, endX)[::-1]:
                    res.append(matrix[endY][i])
            if start < endX and start < endY - 1:
                for i in range(start + 1, endY)[::-1]:
                    res.append(matrix[i][start])

        res = []
        start = 0
        # 必须得 start * 2
        while start * 2 < len(matrix) and start * 2 < len(matrix[0]):
            scan(matrix, len(matrix[0]), len(matrix), start, res)
            start += 1
        return res

solu = Solution()
print solu.spiralOrder([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# -*- coding:utf-8 -*-
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rows = len(matrix)
        colomns = len(matrix[0])
        start = 0
        while colomns > start * 2 and rows > start * 2:
            self.printMatrixCircle(matrix, colomns, rows, start)
            start += 1

    def printMatrixCircle(self, matrix, colomns, rows, start):
        endX = colomns - 1 - start
        endY = rows - 1 - start

        for i in range(start, endX + 1):
            print matrix[start][i]
        if start < endY:
            for i in range(start + 1, endY + 1):
                print matrix[i][endX]
        if start < endX and start < endY:
            for i in range(start, endX)[::-1]:
                print matrix[endY][i]
        if start < endX and start < endY - 1:
            for i in range(start + 1, endY)[::-1]:
                print matrix[i][start]

solu = Solution()
solu.printMatrix([[1,2,3], [4,5,6], [7,8,9]])
solu.printMatrix([[1]])
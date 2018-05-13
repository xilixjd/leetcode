# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Assume that the total area is never beyond the maximum possible value of int.

Credits:
Special thanks to @mithmatt for adding this problem, 
creating the above image and all test cases.
'''


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        def rec_area(x1, y1, x2, y2):
            '''
            x1, y1 是左下角坐标
            x2, y2 是右上角坐标
            :param x1:
            :param y1:
            :param x2:
            :param y2:
            :return:
            '''
            return max(x2 - x1, 0) * max(y2 - y1, 0)
        return rec_area(A, B, C, D) + rec_area(E, F, G, H) - rec_area(max(A, E), max(B, F), min(C, G) , min(D, H))

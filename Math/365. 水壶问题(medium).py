# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例2:

输入: x = 2, y = 6, z = 5
输出: False

'''


class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z > x + y:
            return False
        if x == 0 and y == 0:
            return z == 0
        if x == 0:
            return z % y == 0
        if y == 0:
            return z % x == 0
        if z % x == 0 or z % y == 0:
            return True
        if x < y:
            x, y = y, x
        yushu2 = x % y
        if yushu2 == 0:
            return False
        while yushu2 > 0:
            if z % yushu2 == 0:
                return True
            yushu2 = y % yushu2
        return False

solu = Solution()
print solu.canMeasureWater(22003, 31237, 2)
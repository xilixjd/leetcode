# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给出一个整数，写一个函数来确定这个数是不是3的一个幂。

后续挑战：
你能不使用循环或者递归完成本题吗？

致谢：
特别感谢 @dietpepsi 添加了此问题并且创建了所有的测试用例。
'''


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        import math
        num = math.log(n, 3)
        return abs(num - round(num)) <= 0.00000000001

solu = Solution()
print solu.isPowerOfThree(243)
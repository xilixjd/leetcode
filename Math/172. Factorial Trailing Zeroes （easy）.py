# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        http://blog.csdn.net/feliciafay/article/details/42336835
        计算有多少个 5 就行
        """
        count = 0
        while n > 0:
            k = n / 5
            count += k
            n = k
        return count


    def jiecheng(self, n):
        '''
        用此法会时间复杂度过高
        :param n:
        :return:
        '''
        if n == 0:
            return 1
        total = 1
        for i in range(n):
            total *= (i + 1)
        return total


solu = Solution()
print solu.trailingZeroes(1)
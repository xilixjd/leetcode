# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''


class ReSolution(object):
    def trailingZeroes(self, n):
        """
        25 是 5 * 5 有两个 5
        :type n: int
        :rtype: int
        """
        count = 0
        while n != 0:
            count += n / 5
            n = n / 5
        return count

re = ReSolution()
print re.trailingZeroes(30)


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
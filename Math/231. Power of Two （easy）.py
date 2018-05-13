# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given an integer, write a function to determine if it is a power of two.
2 的幂
'''


class ReSolution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        if n == 1:
            return True
        while n != 0:
            if n == 2:
                return True
            yushu = n % 2
            if yushu != 0:
                return False
            n = n / 2
        return True

re = ReSolution()
print re.isPowerOfTwo(1500000000000)


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return (n & (n - 1)) == 0

    def isPowerOfTwo2(self, n):
        if n < 0:
            return False
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count == 1


solu = Solution()
print solu.isPowerOfTwo2(-4)
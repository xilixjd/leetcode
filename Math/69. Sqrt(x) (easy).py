# -*- coding: utf-8 -*-
'''
Implement int sqrt(int x).

Compute and return the square root of x.

平方根
'''


class ReSolution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        low = 0
        high = x
        while high - low != 1:
            mid = (low + high) / 2
            if mid ** 2 > x:
                high = mid
            elif mid ** 2 < x:
                low = mid
            else:
                return mid
        return low

re = ReSolution()
print re.mySqrt(100)


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        begin = 0
        end = x
        mid = result = 1
        while abs(result - x) > 0.000001:
            mid = float(begin + end) / 2
            result = mid * mid
            if result > x:
                end = mid
            else:
                begin = mid
        return int(mid)

# solu = Solution()
# print solu.mySqrt(3)
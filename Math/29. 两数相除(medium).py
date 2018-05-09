# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        positive_or_not = True
        if (dividend < 0 and divisor) > 0 or (dividend > 0 and divisor) < 0:
            positive_or_not = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while divisor <= dividend:
            temp, i = divisor, 1
            while temp <= dividend:
                dividend -= temp
                res += i
                temp <<= 1
                i <<= 1
        res = res if positive_or_not else -res
        return min(max(-2147483648, res), 2147483647)
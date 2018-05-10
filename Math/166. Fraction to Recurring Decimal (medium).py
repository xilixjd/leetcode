# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given two integers representing the numerator and denominator of a fraction, 
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
 

Credits:
Special thanks to @Shangrila for adding this problem and creating all test cases.
'''


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ""
        if numerator / denominator < 0:
            res += "-"
        if numerator % denominator == 0:
            return str(numerator / denominator)
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator / denominator) + "."
        numerator = numerator % denominator
        numerator_dict = {}
        i = len(res)
        while numerator != 0:
            if numerator_dict.get(numerator) is None:
                numerator_dict[numerator] = i
            else:
                i = numerator_dict[numerator]
                res = res[:i] + "(" + res[i:] + ")"
                return res
            numerator = numerator * 10
            res += str(numerator / denominator)
            numerator %= denominator
            i += 1
        return res

solu = Solution()
print solu.fractionToDecimal(1, 2)
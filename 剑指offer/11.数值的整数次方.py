# -*- coding:utf-8 -*-
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        if exponent > 0:
            exp = exponent
        else:
            exp = -exponent
        calc = 1
        for i in range(exp):
            calc *= base
        if exponent > 0:
            return calc
        else:
            return float(1) / float(calc)

solu = Solution()
print solu.Power(3, -2)
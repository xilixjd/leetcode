# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n。

示例:
给定 n = 2，返回 91。（答案应该是除[11,22,33,44,55,66,77,88,99]外，0 ≤ x < 100 间的所有数字）
'''


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        通项公式为f(k) = 9 * 9 * 8 * ... (9 - k + 2)
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 9
        res = 10
        j = 9
        for i in range(2, n + 1):
            j = temp = 9
            while j >= 9 - i + 2:
                temp *= j
                j -= 1
            res += temp
        return res

solu = Solution()
print solu.countNumbersWithUniqueDigits(3)
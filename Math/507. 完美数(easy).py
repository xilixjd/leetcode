# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。

给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False

 

示例：

输入: 28
输出: True
解释: 28 = 1 + 2 + 4 + 7 + 14
'''


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        def get_divisors(num):
            num_set = set()
            for i in range(1, num / 2 + 1):
                if num % i == 0:
                    num_set.add(i)
            return num_set

        return sum(get_divisors(num)) == num

    def checkPerfectNumber2(self, num):
        import math
        if num <= 1:
            return False
        sums = 0
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                sums += i + num / i
        sums += 1
        return sums == num

solu = Solution()
print solu.checkPerfectNumber2(28)
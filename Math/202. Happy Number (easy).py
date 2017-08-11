# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n_str = str(n)
        sums = 0
        for i in range(len(n_str)):
            sums += pow(int(n_str[i]), 2)
        j = 0
        while sums != 1:
            sums_str = str(sums)
            sums = 0
            for i in range(len(sums_str)):
                sums += pow(int(sums_str[i]), 2)
            j += 1
            if j == 10:
                return False
        return True

solu = Solution()
print solu.isHappy(19)

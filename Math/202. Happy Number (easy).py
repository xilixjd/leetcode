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


class ReSolution(object):
    def isHappy(self, n):
        """
        野鸡解法
        :type n: int
        :rtype: bool
        """
        n_str = str(n)
        sums = 0
        j = 0
        while sums != 1:
            temp = 0
            for n_s in n_str:
                temp += int(n_s) ** 2
            sums = temp
            n_str = str(sums)
            print n_str
            if j > 20:
                return False
            j += 1
        return True

    def isHappy2(self, n):
        '''
        https://leetcode.com/problems/happy-number/discuss/56917/My-solution-in-C(-O(1)-space-and-no-magic-math-property-involved-)
        :param n:
        :return:
        '''
        def get_sum(n_str):
            sums = 0
            for n_s in n_str:
                sums += int(n_s) ** 2
            return sums

        slow = str(n)
        fast = str(get_sum(str(n)))
        while slow != fast:
            slow = str(get_sum(slow))
            fast = str(get_sum(fast))
            fast = str(get_sum(fast))
        return slow == '1'

re = ReSolution()
print re.isHappy(3)


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
# print solu.isHappy(19)

# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


'''


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        sums = 0
        for i in range(len(num_str)):
            sums += int(num_str[i])
        while sums >= 10:
            num_str = str(sums)
            sums = 0
            for i in range(len(num_str)):
                sums += int(num_str[i])
        return sums

solu = Solution()
print solu.addDigits(678)
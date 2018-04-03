# -*- coding: utf-8 -*-
__author__ = 'xilixjd'

'''
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits_str = ''.join([str(d) for d in digits])
        digits_int = int(digits_str)
        digits_int += 1
        digits_str = str(digits_int)
        return [int(d) for d in list(digits_str)]

solu = Solution()
print solu.plusOne([1,2,3])
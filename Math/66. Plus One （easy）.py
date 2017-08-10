# -*- coding: utf-8 -*-
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
        if len(digits) == 0:
            return []
        digits_str_array = [str(d) for d in digits]
        digits_str = ''.join(digits_str_array)
        digits_int = int(digits_str)
        digits_int += 1
        new_digits_str = str(digits_int)
        new_digits_array = list(new_digits_str)
        new_digits = [int(n) for n in new_digits_array]
        return new_digits

solu = Solution()
print solu.plusOne([1,2,9])
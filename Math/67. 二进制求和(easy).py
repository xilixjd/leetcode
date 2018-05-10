# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        array_a = [int(x) for x in list(a)]
        array_b = [int(x) for x in list(b)]
        i = len(a) - 1
        j = len(b) - 1
        max_length = max(i, j) + 2
        temp_length = max_length - 1
        array_res = [0 for f in range(max_length)]
        carry = 0
        while i >= 0 and j >= 0:
            nums = carry + array_a[i] + array_b[j]
            temp = nums % 2
            carry = nums / 2
            array_res[temp_length] = temp
            temp_length -= 1
            i -= 1
            j -= 1
        while i >= 0:
            nums = carry + array_a[i]
            temp = nums % 2
            carry = nums / 2
            array_res[temp_length] = temp
            temp_length -= 1
            i -= 1
        while j >= 0:
            nums = carry + array_b[j]
            temp = nums % 2
            carry = nums / 2
            array_res[temp_length] = temp
            temp_length -= 1
            j -= 1
        if carry > 0:
            array_res[temp_length] = carry
        i = 0
        while i < len(array_res):
            if array_res[i] == 0:
                array_res.pop(i)
            else:
                break
        res = ''.join([str(a) for a in array_res])
        return res if len(res) > 0 else "0"

solu = Solution()
print solu.addBinary("0", "0")
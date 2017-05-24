# -*- coding: utf-8 -*-
'''
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
Note:

The input strings will not have extra blank.
The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. 
And the output should be also in this form.
'''

class Solution(object):
    def complexNumberMultiplyMy(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        array_a = a.split('+')
        array_b = b.split('+')
        real_a = array_a[0]
        real_b = array_b[0]
        i_a = array_a[1]
        i_b = array_b[1]
        real_num1 = int(real_a) * int(real_b)
        i_num1 = int(real_a) * int(i_b[:-1])
        i_num2 = int(i_a[:-1]) * int(real_b)
        i_num = i_num1 + i_num2
        i2_num = int(i_a[:-1]) * int(i_b[:-1])
        if i2_num == 0:
            s = str(real_num1) + '+' + str(i_num) + 'i'
            return s
        else:
            s = str(real_num1 - i2_num) + '+' + str(i_num) + 'i'
            return s


solu = Solution()
print solu.complexNumberMultiplyMy('1+-1i', '1+-1i')
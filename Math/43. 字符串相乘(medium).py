# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        products = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1))[::-1]:
            for j in range(len(num2))[::-1]:
                p1 = ord(num1[i]) - ord("0")
                p2 = ord(num2[j]) - ord("0")
                print num1[i], num2[j], p1, p2, p1 * p2, i + j + 1
                products[i + j + 1] += p1 * p2
        carry = 0
        for i in range(len(products))[::-1]:
            temp = (products[i] + carry) % 10
            carry = (products[i] + carry) / 10
            products[i] = temp
        print products
        i = 0
        while i < len(products):
            if products[i] == 0:
                products.pop(i)
            else:
                break
        print products
        res = [str(p) for p in products]
        return "".join(res) if len(res) != 0 else 0

re = Solution()
print re.multiply('10', '10')
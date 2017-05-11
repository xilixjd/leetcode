# -*- coding: utf-8 -*-

'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def multiplyMy(self, num1, num2):
        """
        不符题意！！
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num_dict = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
        }
        int_num1 = int_num2 = 0
        i = j = 0
        for n in num1[::-1]:
            int_num1 += num_dict[n] * (10 ** i)
            i += 1
        for n in num2[::-1]:
            int_num2 += num_dict[n] * (10 ** j)
            j += 1
        return str(int_num1 * int_num2)

    def multiplyFast(self, num1, num2):
        products = [0 for i in range(len(num1) + len(num2))]
        for i in range(len(num1))[::-1]:
            for j in range(len(num2))[::-1]:
                d1 = ord(num1[i]) - ord('0')
                d2 = ord(num2[j]) - ord('0')
                products[i + j + 1] += d1 * d2
        carry = 0
        for i in range(len(products))[::-1]:
            temp = (products[i] + carry) % 10
            carry = (products[i] + carry) / 10
            products[i] = temp

        while len(products) != 0 and products[0] == 0:
            products.pop(0)
        if len(products) == 0:
            return "0"
        return ''.join([str(p) for p in products])

solu = Solution()
print solu.multiplyFast('0', '1')
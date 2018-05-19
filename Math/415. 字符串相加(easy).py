# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def get_sub(num_c):
            return ord(num_c) - ord("0")

        array = []
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >= 0 and j >= 0:
            num = carry + get_sub(num1[i]) + get_sub(num2[j])
            temp = num % 10
            carry = num / 10
            array.append(str(temp))
            i -= 1
            j -= 1
        while i >= 0:
            num = carry + get_sub(num1[i])
            temp = num % 10
            carry = num / 10
            array.append(str(temp))
            i -= 1
        while j >= 0:
            num = carry + get_sub(num2[j])
            temp = num % 10
            carry = num / 10
            array.append(str(temp))
            j -= 1
        if carry == 1:
            array.append("1")
        array.reverse()
        return "".join(array)

solu = Solution()
print solu.addStrings("0", "0")
# -*- coding: utf-8 -*-

'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''


class Solution(object):
    def addBinaryMy(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        i = len(a) - 1
        j = len(b) - 1
        a = list(a)
        b = list(b)
        result = [0 for i in range(max(len(a), len(b)) + 1)]
        k = max(len(a), len(b))
        carry = 0
        while len(a) != 0 and len(b) != 0:
            temp = (int(a[-1]) + int(b[-1]) + carry) % 2
            carry = (int(a[-1]) + int(b[-1]) + carry) / 2
            result[k] = temp
            a.pop()
            b.pop()
            k -= 1
        while len(a) != 0:
            temp = (int(a[-1]) + carry) % 2
            carry = (int(a[-1]) + carry) / 2
            result[k] = temp
            a.pop()
            k -= 1
        while len(b) != 0:
            temp = (int(b[-1]) + carry) % 2
            carry = (int(b[-1]) + carry) / 2
            result[k] = temp
            b.pop()
            k -= 1
        if carry == 1:
            result[k] = carry
        for i in range(len(result)):
            if result[i] != 0:
                string = ''.join([str(j) for j in result[i:]])
                return string
        return "0"


solu = Solution()
print solu.addBinaryMy("1", "1")
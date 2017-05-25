# -*- coding: utf-8 -*-
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5
Note: Do not use the eval built-in library function.
'''
import math

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if not s[i].isdigit() and not s[i].isspace() or i == len(s) - 1:
                if sign == '+':
                    pass
                elif sign == '-':
                    num = -num
                elif sign == '*':
                    num = num * stack[-1]
                    stack.pop()
                elif sign == '/':
                    num = self.get_division(stack[-1], num)
                    stack.pop()
                stack.append(num)
                num = 0
                sign = s[i]
        value = 0
        while len(stack) > 0:
            value += stack.pop()
        return value

    def get_division(self, num1, num2):
        if num2 == 0:
            return False
        if num1 > 0 and num2 > 0:
            return num1 / num2
        else:
            if num2 < 0:
                num2 = -num2
            if num1 < 0:
                num1 = -num1
            return -(num1 / num2)


solu = Solution()
print solu.calculate('14-3/2')

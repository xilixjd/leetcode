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


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return
        array = []
        value_str = ""
        for i in range(len(s)):
            if s[i].isdigit():
                value_str += s[i]
            else:
                array.append(int(value_str))
                value_str = ""
                if s[i].isspace():
                    continue
                if s[i] == '+':
                    array.append('+')
                    continue
                if s[i] == '*' or s[i] == '/'


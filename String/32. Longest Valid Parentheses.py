# -*- coding: utf-8 -*-

'''
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''


class Solution(object):
    def longestValidParenthesesMy(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return 0
        array = []
        # count = 0
        max_count = 0
        # x = {}
        y = []
        for i in range(0, len(s)):
            if s[i] == '(':
                array.append({i: '('})
                # x[i] = '('
            elif s[i] == ')':
                if len(array) != 0 and array[-1][array[-1].keys()[0]] == '(':
                    y.append([array[-1].keys()[0], i])
                    array.pop()
                    # count += 2
                else:
                    array.append({i: ')'})
        a = []
        for j in y:
            a += j
        a.sort()
        print a
        return self.getConsecutiveNumsLen(a)

    def getConsecutiveNumsLen(self, array):
        if len(array) == 0:
            return 0
        max_len = 0
        leng = 0
        for i in range(1, len(array)):
            if array[i] - array[i - 1] == 1:
                leng += 1
            else:
                leng = 0
            max_len = max(max_len, leng)
        return max_len + 1

solu = Solution()
print solu.longestValidParenthesesMy('()')
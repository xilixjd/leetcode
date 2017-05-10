# -*- coding: utf-8 -*-

'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''


class Solution(object):
    def countAndSayMy(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return
        s = "1"
        for i in range(n-1):
            s = self.generateNext(s)
        return s

    def generateNext(self, s):
        s += '0'
        # print s
        item = s[0]
        count = 1
        string = ""
        for i in range(1, len(s)):

            if s[i] == item:
                count += 1
            else:
                string += str(count) + item
                item = s[i]
                count = 1
        return string

solu = Solution()
print solu.countAndSayMy(1)
# print solu.generateNext('21')
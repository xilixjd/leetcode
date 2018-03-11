# -*- coding: utf-8 -*-

'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

class ReSolution(object):
    def numDecodings(self, s):
        """
        思路：
        array[i] 表示 s[0..i-1] 的解码方法
        则有 array[i] = array[i - 1] + array[i - 2]
        且有以下限制：
        1。s[i - 1] 不能为 0，若为 0 则 array[i] = array[i - 2]
        2。s[i - 2: i] 中第一个数不能为 0，且 s[i - 2: i] 数必须在 1-26 之间
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0] == "0":
            return 0
        array = [0 for i in range(len(s) + 1)]
        array[0] = 1
        array[1] = 1
        for i in range(2, len(array)):
            if s[i - 1] != "0":
                array[i] = array[i - 1]
            if s[i - 2] != "0":
                temp = int(s[i - 2: i])
                if 0 < temp <= 26:
                    array[i] += array[i - 2]
        return array[len(s)]

re = ReSolution()
print re.numDecodings('01')


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        类似爬楼梯问题，但要加很多限制条件。
        定义数组number，number[i]意味着：字符串s[0..i-1]可以有number[i]种解码方法。
        回想爬楼梯问题一样，number[i] = number[i-1] + number[i-2]
        但不同的是本题有多种限制：
        第一： s[i-1]不能是0，如果s[i-1]是0的话，number[i]就只能等于number[i-2]
        第二，s[i-2,i-1]中的第一个字符不能是0，而且Integer.parseInt(s.substring(i-2,i))获得的整数必须在0到26之间。

        1010，生成的number数组为：[1,1,1,1,1]
        10000，生成的number数组为：[1,1,1,0,0,0,0,0,0]
        """
        if len(s) == 0:
            return 0
        if s[0] == "0":
            return 0
        number = [0 for i in range(len(s) + 1)]
        number[0] = 1
        number[1] = 1
        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                number[i] = number[i - 1]
            if s[i - 2] != "0":
                temp = int(s[i - 2:i])
                if 0 < temp <= 26:
                    number[i] += number[i - 2]
        print number
        return number[len(s)]


solu = Solution()
print solu.numDecodings('01')
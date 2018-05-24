# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
'''


class Solution(object):
    def numDecodings(self, s):
        """
        丑陋的实现方法，不如判断 != 0 的情况
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, len(dp)):
            if s[i - 2] == "0":
                if s[i - 1] == "0":
                    return 0
                dp[i] = dp[i - 1]
            elif s[i - 1] == "0":
                if int(s[i - 2: i]) > 20:
                    return 0
                dp[i] = dp[i - 2]
            elif int(s[i - 2: i]) > 26:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        # print dp

        return dp[len(s)]

solu = Solution()
print solu.numDecodings("17")

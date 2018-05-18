# -*- coding: utf-8 -*-
__author__ = 'xilixjd'


'''

给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

示例 1:

输入:
8

输出:
3

解释:
8 -> 4 -> 2 -> 1
示例 2:

输入:
7

输出:
4

解释:
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1
'''


class Solution(object):
    def integerReplacement(self, n):
        """
        超时
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n == 2:
            return 1
        dp = [100000 for i in range(n + 1)]
        if n % 2 != 0:
            dp.append(1)
        dp[n] = 0
        for i in range(2, len(dp) - 2)[::-1]:
            min_val = dp[i]
            if i * 2 <= len(dp) - 1:
                min_val = min(min_val, dp[i * 2] + 1)
            if i % 2 == 0:
                min_val = min(min(dp[i + 1], dp[i - 1]) + 1, min_val)
            else:
                dp[i + 1] = min(dp[i + 1], min_val + 1)
                dp[i - 1] = min(dp[i - 1], min_val + 1)
            dp[i] = min_val
        return dp[2] + 1

    def integerReplacement2(self, n):
        help_dict = {}

        def helper(n):
            print n
            if n == 1:
                return 0
            if help_dict.get(n) is not None:
                return help_dict[n]
            if n % 2 == 0:
                val = helper(n / 2) + 1
            else:
                val = min(helper(n - 1), helper(n + 1)) + 1
            help_dict[n] = val
            return val

        return helper(n)


solu = Solution()
print solu.integerReplacement2(11)